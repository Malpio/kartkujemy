from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('registry/', views.registryPage, name='registry'),
    path('logout/', views.logoutPage, name='logout')
]