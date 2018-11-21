# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:06:15 2018

@author: eric
"""

from django.urls import path, re_path

from . import views

# app_name is a namespace varaible
app_name = 'inputs'
urlpatterns = [
    path('', views.index, name='index'),

    path('broker_form/', views.broker_form, name='broker_form'),

    re_path('lender/(?P<pk>[0-9]+)/$', views.lender_detail, name='lender_detail'),
    re_path('lender_form/(?P<pk>[0-9]+)/$', views.edit_lender_form, name='edit_lender_form'),
    path('lender_form/', views.lender_form, name='lender_form'),
    path('lender_list/', views.lender_list, name='lender_list'),

    re_path('loan/(?P<pk>[0-9]+)/$', views.loan_detail, name='loan_detail'),
    re_path('loan_form/(?P<pk>[0-9]+)/$', views.edit_loan_form, name='edit_loan_form'),
    path('loan_form/', views.loan_form, name='loan_form'),
    path('loan_list/', views.loan_list, name='loan_list'),

    path('ajax/load_loantype_form/', views.load_loantype_form , name = 'load_loantype_form'),
]
