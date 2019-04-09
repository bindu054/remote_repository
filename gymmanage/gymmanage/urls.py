"""gymmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from appgym import views
from appgym.views import adviewplans, updateplan, deleteplan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('openadd/', views.openadd),
    path('login/', views.adlogin),
    path('user/', views.user),
    path('userss/', views.showuserlogin),
    path('ulogin/', views.userlogin),
    path('uregister/', views.uregister),
    path('register/', views.register),
    path('addplan/', views.addplan),
    path('viewsuggestions/', views.viewsuggestions),
    path('payment/', views.payment),
    path('viewuser/', views.viewuser),
    path('viewplans/', views.viewplans),
    path('paymentp/', views.paymentp),
    path('suggestion/', views.suggestion),
    path('viewprofile/', views.viewprofile),
    path('update/', views.update),
    path('updateuser/', views.updateuser),
    path('usuggestion/', views.usuggestion),
    path('viewplans/', views.userviewplans),
    path('admplans/', views.admplans),
    path('paymentaf/', views.paymentaf),
    path('back/', views.back),
    path('newregister/', views.newregister),
    path('delete/', views.delete),
    path('confirmdel/', views.confirmdel),
    path('adminlogout/', views.adminlogout),
    path('userlogout/', views.userlogout),
    path('backuser/', views.backuser),
    path('deleteuser/', views.deleteuser),
    path('adminviewplan/', adviewplans.as_view()),
    path('update<str:pk>/', updateplan.as_view()),
    path('uppie/', adviewplans.as_view()),
    path('deleteplan<str:pk>/', deleteplan.as_view()),
    path('delview/', adviewplans.as_view()),
    # path('forgetpass/',forgetpass.as_view()),
    path('join/', views.join),
    path('viewusersuggestions/', views.viewusersuggestions),
    path('previoussuggestions/', views.previoussuggestions),
    # path('delsugg/',views.delsugg),
    path('goback/', views.goback),
    path('deleteusersuggestion/', views.deleteusersuggestion),
    path('conuserdel/', views.conuserdel),
    path('aboutus/', views.aboutus),
    path('home/', views.home),
    path('delhi/', views.deleteaduser),
    path('viewuserupdate/', views.viewuserupdate),
    path('userdataupdate/', views.updateuadd),
    path('forgetpassword/', views.forgetpassword),
    path('forgottenpassword/', views.getpass),

]
