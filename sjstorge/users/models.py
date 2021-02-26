# -*- coding: utf-8 -*-#
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class UserProfile(AbstractUser):
    """用户表"""
    company = models.CharField(max_length=300, default='', verbose_name='公司名称')
    tax_id = models.CharField(max_length=50, default='', verbose_name='纳税人识别号')
    boss_name = models.CharField(max_length=100, default='', verbose_name='法定代表人')
    telephone = models.CharField(max_length=200, default='', verbose_name='手机号')
    # 一对一，放在实体端
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.company