from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }

@admin.register(models.Comment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user')

admin.site.register(models.Category)
