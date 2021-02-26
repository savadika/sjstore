# -*- coding: utf-8 -*-#
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile

# Create your models here.
class UpfileInfo(models.Model):
    """用户信息上传"""
    name = models.CharField(max_length=200,default='',verbose_name='公司名称')
    images = models.CharField(max_length=300,default='',verbose_name='上传图片')
    video = models.CharField(max_length=200,default='',verbose_name='上传视频')
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    class Meta:
        verbose_name="真实信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name











