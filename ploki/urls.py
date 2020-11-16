from django.urls import path
from . import views

app_name = 'ploki'

urlpatterns = [
    path('latest/', views.ploki_latest, name='ploki_latest'),
    path('ploki/<int:pk>/', views.ploki_detail, name='ploki_detail'),
    path('ploki/', views.ploki_index, name='ploki_index'),
    path('graph/', views.graph, name='graph'),
    path('printed/', views.html_to_pdf_view, name='printruno'),
    path('<category>/', views.ploki_category, name='ploki_category'),
    path('api/play_count_by_month/', views.play_count_by_month, name='play_count_by_month'),
]
