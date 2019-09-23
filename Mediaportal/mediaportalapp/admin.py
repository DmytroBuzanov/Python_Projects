from __future__ import unicode_literals
from django.contrib import admin
from mediaportalapp.models import Category, Article

class ArticleAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)



# Register your models here.
