from django.urls import path
from .import  views

urlpatterns=[
     path('signup/',views.register, name='index'),
     path('generator_register/',views.generator_register.as_view(), name='generator_register'),
     path('handler_register/',views.handler_register.as_view(), name='handler_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]