#!/usr/bin/env python

"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import fastspecfit.webapp.sample.views as sample

urlpatterns = [
    path('', sample.explore, name='index'),
    path('target/', sample.nice_target_name, name='nice_target_name'),
    path('target-prev/', sample.target_prev, name='target-prev'),
    path('target-next/', sample.target_next, name='target-next'),

]

