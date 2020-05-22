from django.contrib import admin

from .models import Post, Category, Play


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Otsikko',               {'fields': ['title']}),
        ('Tarina',               {'fields': ['body']}),
        ('Luokittele',               {'fields': ['categories']}),
        ('Kuvita tarinaa',               {'fields': ['kuvitusta']}),
        ('Kuvita tarinaa',               {'fields': ['kuvitusta2']}),
        ('Kuvita tarinaa',               {'fields': ['kuvitusta3']}),
        ('Julkaisu päivä',               {'fields': ['julkaistu_pvm']}),
    ]
    list_display = ('title', 'created_on')
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Play)
