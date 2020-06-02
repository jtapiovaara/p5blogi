from django.contrib import admin

from .models import Post, Category, Play

admin.site.site_header = 'Blogin ylläpito'
admin.site.site_title = 'p5blogi'


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Otsikko', {'fields': ['title']}),
        ('Tarina ja luokittelu',  {'fields': [('body', 'categories')]}),
        # ('Luokittele',  {'fields': ['categories']}),
        ('Kuvita tarinaa',  {'fields': [('kuvitusta', 'kuvitusta2', 'kuvitusta3')]}),
        ('Julkaisu päivä',  {'fields': ['julkaistu_pvm']}),
    ]

    list_display = ('title', 'julkaistu_pvm')
    list_filter = ('julkaistu_pvm',)
    date_hierarchy = 'julkaistu_pvm'
    ordering = ('-julkaistu_pvm',)
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'kuva']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Play)
