from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.boss_signup),
    path('signup/worker/', views.worker_signup),

    path('login/', views.login),

    path('logintest/', views.is_authenticated_api),
]
