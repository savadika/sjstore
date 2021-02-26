# -*- coding: utf-8 -*-#
from django.shortcuts import render

# Create your views here.

from models import Course, Student
from django.views.generic import View
from .models import Course, Student
from django.http import HttpResponse

class TestAddView(View):
    """
    单个测试添加
    先分别取出不同的模型，再进行关联操作
    """
    def get(self, request):
        course1 = Course.objects.get_or_create(course_name='math')
        student1 = Student.objects.get_or_create(name='ylf', sex='male')
        # 添加操作
        # 因course1 返回的是一个元组（course1 , True/False）
        my_course1 = course1[0]
        my_student1 = student1[0]
        # 添加操作
        my_student1.course.add(my_course1)
        return HttpResponse("add ok")

class QualityAddView(View):
    def get(self, request):
        """测试批量添加关联,必须要从有外键的模型处进行添加"""
        course2 = Course.objects.get(course_name='yuwen')    # object
        females = Student.objects.filter(sex='female').all()  # [student1 , student2]
        # 方法1，循环
        # for female in females:
        #     female.course.add(course2)
        # return HttpResponse("quality add ok")
        # 方法2，解包方法，给student2 添加所有的课程
        student2 = Student.objects.get(name='cjq')
        courses = Course.objects.all()
        student2.course.add(*courses)
        return HttpResponse("quality add ok")




class TestSingleRemoveView(View):
    def get(self, request):
        """
        删除关联关系
        思路：找到模型，调用remove方法，注意：也是要从有外键的一侧进行删除
        """
        course3 = Course.objects.get(course_name='english')
        # 单个学生删除
        student3 = Student.objects.get(name='ylf')
        student3.course.remove(course3)
        return HttpResponse("single student removed")

class QualityRemoveView(View):
    def get(self, request):
        """
        批量删除
        1  按照单个删除+循环的办法
        2  其他需求（删除和课程3有关的所有数据）
        """
        #  反向批量删  删除和课程3有关的所有数据
        # course3 = Course.objects.get(course_name='english')
        # students = Student.objects.all()
        # course3.student_set.remove(*students)

        # 正向批量删  删除2号学生的相关数据
        # stu2 = Student.objects.get(name='cjq')
        # courses =Course.objects.all()
        # stu2.course.remove(*courses)
        # return HttpResponse("quality removed")

        # 第三种  删除2号学生的所有数据
        student2 = Student.objects.get(name='cjq')
        student2.course.clear()
        return HttpResponse('all clear')


class TestSingleUpdate(View):
    """
    测试单个修改
    将关联表里面的studentid=1，course_id=1的数据更新为studentid=1,courseid=2
    """
    def get(self, request):
        # 场景1,修改中间表：将学生id=1的学生，选修课程从math改为语文
        # stuentsid=1 ，course_id =1 的学生数据修改为 student_id =1, couse_id =2
        # 方法1 ，先删除旧的数据，再添加新的数据
        course1 = Course.objects.get(course_name='math')
        student1 = Student.objects.get(id=1)
        student1.course.remove(course1)
        course2 = Course.objects.get(course_name='yuwen')
        student1.course.add(course2)
        return HttpResponse('all changed!')
        # 方法2，直接修改中间表,这个目前来看是做不到
        # 只能通过第三张表来做到了
        # https://blog.csdn.net/qq_40576301/article/details/100566999




class TestQueryView(View):
    """测试多对多查询"""
    def get(self, request):
        # 正向查询 ,单条【姓名为ylf的学生的所有课程】
        courses = Student.objects.get(name='ylf').course.all()
        # 反向查询[学数学的学生，同时为女生的人]
        student1 = Course.objects.get(course_name='math').student_set.filter(sex='female').all()
        # 反向查询2，基于双下划线的跨表查询，直接查值【查询选修语文课程的所有学生姓名】,两种方式等价
        current_student = Course.objects.get(course_name='yuwen').student_set.values("name")
        current_student2 = Course.objects.filter(course_name='yuwen').values("student__name")
        # 查询数量
        current_count = Course.objects.get(course_name='yuwen').student_set.values("name").count()
        # F查询 和 Q 查询


        
        return HttpResponse('all queryed!')











