from django.contrib import admin


# Register your models here.
from .models import *

from modeltranslation.admin import TranslationAdmin

@admin.register(Info)
class InfoAdmin(TranslationAdmin):
	prepopulate_fields = {'slug': ('title',)}

admin.site.register(User)
admin.site.register(ProfileContent)
admin.site.register(TextContent)
admin.site.register(ImgContent)
admin.site.register(ContentType)