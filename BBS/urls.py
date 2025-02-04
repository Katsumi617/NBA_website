from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('reg/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('prof/', views.user_profile, name='profile'),
    path('profedit/', views.edit_profile, name='profile-edit'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
]