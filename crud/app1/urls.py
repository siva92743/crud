from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_register', views.user_register, name='user_register'),
    path('user_view', views.user_view, name='user_view'),
    path('user_view2', views.user_view2, name='user_view2'),
    path('user_update/<int:id>/', views.user_update, name='user_update'),
    path('user_delete/<int:id>/', views.user_delete, name='user_delete'),
]
