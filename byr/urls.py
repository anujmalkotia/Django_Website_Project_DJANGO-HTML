"""byr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from .views import home_page,pcb_page,bbu_page,aayush_page,abhishek_page,rahul_page,soumava_page,bhasmag_page,ashwani_page,bg_page,gs_page,starter_page,starterpcplus_page,streamingpc_page,creator_page,home_page1,blog_page,gs1_page,gs2_page,gs3_page,gs4_page,gs5_page,gs6_page,gs7_page,gs8_page,aboutus_page,starter1_page,starter2_page,starter3_page,starter4_page,starter5_page,starter6_page,starterp1_page,starterp2_page,starterp3_page,starterp4_page,starterp5_page,starterp6_page,stream1_page,stream2_page,stream3_page,stream4_page,stream5_page,stream6_page,creator1_page,creator2_page,creator3_page,creator4_page,creator5_page,creator6_page

urlpatterns = [
    path('',home_page),
    path('pcb',pcb_page),
    path('admin/', admin.site.urls),
    path('bbu',bbu_page),
    path('aayush',aayush_page),
    path('abhishek',abhishek_page),
    path('rahul',rahul_page),
    path('soumava',soumava_page),
    path('bhasmag',bhasmag_page),
    path('ashwani',ashwani_page),
    path('bg',bg_page),
    path('gs',gs_page),
    path('starter',starter_page),
    path('starterpcplus',starterpcplus_page),
    path('streamingpc',streamingpc_page),
    path('creator',creator_page),
    path('hp',home_page1),
    path('blogs',blog_page),
    path('gs1',gs1_page),
    path('gs2',gs2_page),
    path('gs3',gs3_page),
    path('gs4',gs4_page),
    path('gs5',gs5_page),
    path('gs6',gs6_page),
    path('gs7',gs7_page),
    path('gs8',gs8_page),
    path('aboutus',aboutus_page),
    path('starter1',starter1_page),
    path('starter2',starter2_page),
    path('starter3',starter3_page),
    path('starter4',starter4_page),
    path('starter5',starter5_page),
    path('starter6',starter6_page),
    path('starter+1',starterp1_page),
    path('starter+2',starterp2_page),
    path('starter+3',starterp3_page),
    path('starter+4',starterp4_page),
    path('starter+5',starterp5_page),
    path('starter+6',starterp6_page),
    path('stream1',stream1_page),
    path('stream2',stream2_page),
    path('stream3',stream3_page),
    path('stream4',stream4_page),
    path('stream5',stream5_page),
    path('stream6',stream6_page),
    path('creator1',creator1_page),
    path('creator2',creator2_page),
    path('creator3',creator3_page),
    path('creator4',creator4_page),
    path('creator5',creator5_page),
    path('creator6',creator6_page),
]
