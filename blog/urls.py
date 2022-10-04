from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('article/', views.article , name='blog-article')
]
