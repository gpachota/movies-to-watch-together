from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('list/<int:pk>/', views.list_detail, name='list_detail')
]
