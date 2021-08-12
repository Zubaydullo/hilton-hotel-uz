from django.contrib import admin
from modeltranslation import translator
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


admin.site.register(BlogComment)
# admin.site.register(Blog)


class BlogAdmin(TranslationAdmin):
    model = Blog

admin.site.register(Blog, BlogAdmin)