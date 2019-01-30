from django.urls import path
from . import views
from Test import views as views_tests

urlpatterns = [
    path('', views.home, name="TakeTest-Home"),
    path('home/', views.home, name="TakeTest-Home"),
    path('about/', views.about, name="TakeTest-About"),
    path('post/', views_tests.post, name="Test-Post")
]
