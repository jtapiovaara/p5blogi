from django.forms import ModelForm
import django_filters
from .models import Post


class SuodataPosti(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'body': ['icontains']
        }
