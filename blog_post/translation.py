from modeltranslation.translator import translator,register, TranslationOptions
from .models import *


class BlogTranslationOptions(TranslationOptions):
    fields = ('blog_heading', 'blog_text',)

translator.register(Blog, BlogTranslationOptions)


