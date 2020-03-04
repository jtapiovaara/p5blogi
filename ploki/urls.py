from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from . import views
from .models import Post

app_name = 'ploki'

urlpatterns = [
    path('', views.ploki_index, name='ploki_index'),
    path('<int:pk>/', views.ploki_detail, name='ploki_detail'),
    path('<category>/', views.ploki_category, name='ploki_category'),
    # path('archive/', ArchiveIndexView.as_view(model=Post, date_field="pub_date"), name="archive"),
]