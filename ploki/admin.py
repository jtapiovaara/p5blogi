from django.contrib import admin

from .models import Post, Category, Play, Comment

admin.site.site_header = 'Blogin ylläpito'
admin.site.site_title = 'p5blogi'


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Otsikko', {'fields': ['title']}),
        ('Tarina ja luokittelu',  {'fields': [('body', 'categories')]}),
        # ('Luokittele',  {'fields': ['categories']}),
        ('Kuvita tarinaa',  {'fields': [('kuvitusta', 'kuvitusta2', 'kuvitusta3')]}),
        ('Lisää linkki lisätietoihin (ei pakollinen)',  {'fields': [('linkkinimi', 'linkki')]}),
        ('Julkaisu päivä',  {'fields': ['julkaistu_pvm']}),
    ]

    list_display = ('title', 'julkaistu_pvm')
    list_filter = ('julkaistu_pvm',)
    date_hierarchy = 'julkaistu_pvm'
    ordering = ('-julkaistu_pvm',)
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_author', 'comment_created_on']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'kuva']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Play)
