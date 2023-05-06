from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import userregisterform, profileform
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.


class registerview(CreateView):
    form_class = userregisterform
    #success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('project_list')


@login_required
def editprofile(request):
    if request.method == 'POST':
        form = profileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = profileform(instance=request.user)
        return render(request, 'profile.html', {
            'form': form
        })



