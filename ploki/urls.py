from django.urls import path
from django.conf.urls import url
from . import views
from .views import graph, play_count_by_month
from .models import Post

app_name = 'ploki'

urlpatterns = [
    path('latest/', views.ploki_latest, name='ploki_latest'),
    path('ploki/<int:pk>/', views.ploki_detail, name='ploki_detail'),
    path('ploki/', views.ploki_index, name='ploki_index'),
    path('graph/', views.graph, name='graph'),
    path('printed/', views.html_to_pdf_view, name='printruno'),
    path('<category>/', views.ploki_category, name='ploki_category'),
    # url(r'^ploki/api/play_count_by_month', play_count_by_month, name='play_count_by_month'),
    path('api/play_count_by_month/', views.play_count_by_month, name='play_count_by_month'),
]
