from django.urls import path
from myapp import views

app_name = 'relative'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.Register,name='register'),
    path('ulogin/',views.Ulog,name='ulogin'),
    path('login/',views.UserLogin,name='login'),
    path('out/',views.Out,name='out'),

]