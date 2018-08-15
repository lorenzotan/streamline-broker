# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:06:15 2018

@author: eric
"""

from django.urls import path

from . import views

# app_name is a namespace varaible 
app_name = 'inputs'
urlpatterns = [
    path('lender_nav/'   , views.lender_nav  , name = 'lender_nav'),
    path('lender_form/'  , views.lender_form , name = 'lender_form'),
    path('lender_list/'  , views.lender_list , name = 'lender_list'),
    path('loan_nav/'     , views.loan_nav  , name = 'loan_nav'),
    path('loan_form/'    , views.loan_form , name = 'loan_form'),
    path('loan_list/'    , views.loan_list , name = 'loan_list'),
]
