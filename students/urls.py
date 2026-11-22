from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('edit/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]