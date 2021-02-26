# -*- coding: utf-8 -*-#
from django.conf.urls import url, include
from .views import  TestAddView, QualityAddView, TestSingleRemoveView, QualityRemoveView
from .views import  TestSingleUpdate, TestQueryView

urlpatterns=[
    # 测试多对多添加
    url(r'^testadd/$', TestAddView.as_view(), name='testadd'),
    # 测试批量添加
    url(r'^quadd/$', QualityAddView.as_view(), name='quadd'),
    # 测试删除
    url(r'^singleremove/$', TestSingleRemoveView.as_view(), name='testremove'),
    # 测试批量删除
    url(r'^quremove/$', QualityRemoveView.as_view(), name='quremove'),
    # 测试更新
    url(r'^testupdate/$', TestSingleUpdate.as_view(), name='testupdate'),
    # 测试查询
    url(r'^testquery/$', TestQueryView.as_view(), name='testquery')
]