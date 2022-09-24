from django.db import models
from django.contrib import auth
from django.contrib.auth.models import Group

# Create your models here.

class Homework(models.Model):
    title = models.CharField('标题', max_length=50, empty=False)
    group = models.ForeignKey(Group, models.SET_NULL, help_text='需要完成该作业的组')
    date = models.DateTimeField(auto_now_add=True)


class HwStatus(models.Model):
    user = models.ForeignKey(auth.get_user_model(), models.CASCADE)
    homework = models.ForeignKey(Homework, models.CASCADE)
    status = models.CharField('状态', max_length=14, empty=True, null=False, default='')



