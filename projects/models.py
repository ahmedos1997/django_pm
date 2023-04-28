from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):             # ستعيد لنا نتيجة عند تحويل الصنف الى سلسلة نصية
        return self.name


class projectstatus(models.IntegerChoices): # لتحديد نوع الحالة الخاصة ب project
    PENDING = 1, 'pending'
    COMPLETED = 2, 'completed'
    POSTPONED = 3, 'postponed'
    CANCELLED = 4, 'cancelled'


class project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(category, on_delete=models.PROTECT)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=projectstatus.choices,
        default=projectstatus.PENDING
    )

    def __str__(self):
        return self.title

class task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    def __str__(self):
        return self.description


