from django import template
from home.models import *

register = template.Library()

@register.simple_tag()
def getInfo(filt=None, selected=0):
	if not filt:
		return Info.objects.filter(is_pub=True)
	else:
		return Info.objects.filter(pk__gt=filt, is_pub=True)

@register.simple_tag()
def ThisProfileContent(pageuser=None):
	if not pageuser:
		pass
	else:
		return ProfileContent.objects.filter(profile=pageuser)

@register.simple_tag()
def getTextContent(name=None):
	if not name:
		pass
	else:
		return TextContent.objects.get(name=name)

@register.simple_tag()
def getImgContent(name=None):
	if not name:
		pass
	else:
		return ImgContent.objects.get(name=name)

@register.simple_tag()
def getTypes():
	return ContentType.objects.all()

