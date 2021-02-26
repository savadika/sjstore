# -*- coding: utf-8 -*-#
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Course(models.Model):
    """多对多--学生，选修课"""
    course_name = models.CharField(max_length=100, default='', verbose_name='课程名称')


class Student(models.Model):
    """多对多--学生，选修课"""
    name = models.CharField(max_length=100, default='', verbose_name='姓名')
    sex = models.CharField(max_length=8, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    course = models.ManyToManyField(Course)


