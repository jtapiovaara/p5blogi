from django.urls import path
from . import views

app_name = 'ploki'

urlpatterns = [
    path('', views.ploki_index, name='ploki_index'),
    path('<int:pk>/', views.ploki_detail, name='ploki_detail'),
    path('<category>/', views.ploki_category, name='ploki_category'),
]