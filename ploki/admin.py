from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Otsikko',               {'fields': ['title']}),
        ('Tarina',               {'fields': ['body']}),
        ('Luokittele',               {'fields': ['categories']}),
    # ('Luokittele',               {'fields': [Category.name]}), Tähän pitäisi saada näykyville Cat nimi, ei tunniste
    ]
    list_display = ('title', 'created_on')
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)