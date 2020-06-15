from django.urls import path, re_path, include

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('over-ons', views.over_ons, name='over_ons'),
    path('<slug:slug>/', views.detail, name='detail')
]
