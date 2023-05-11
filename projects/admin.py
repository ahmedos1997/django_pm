from django.contrib import admin
from . import models
from django.db.models import Count

# Register your models here.

admin.site.register(models.category)


@admin.register(models.project)
class project_admin(admin.ModelAdmin):
    list_display = ['title','status','user','category','created_at','task_count'] # تحديد المارد عرضه
    list_per_page = 20 # تحديد عدد المشارع في الصفحة الواحدة
    list_editable = ['status'] # امكانية التعديل مباشرة من الاعمدة

    def task_count(self, obj): # لعدم وجود خاصية جمع ل task انشئنا هذه الدالة
        return obj.task_count # استدعينا عملية الجمع التي في الاسفل

    def get_queryset(self, request):   # دالة لتخفيف عملية الاستعلامات على القاعدة
        query = super().get_queryset(request)
        query = query.annotate(task_count=Count('task')) # عملية الجمع
        return query





@admin.register(models.task)
class task_admin(admin.ModelAdmin):
    list_display = ['id','description','project','is_completed']
    list_editable = ['is_completed']
    list_per_page = 20