from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<str:room>/<str:created>/', views.video, name='video'),
    path("new_meet/", views.new_meet, name='new_meet'),
]