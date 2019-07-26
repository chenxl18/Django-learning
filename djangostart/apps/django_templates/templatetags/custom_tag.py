"""
@file:custom_tag.py
@author:陈先乐
@date:2019/07/26
"""
from django import template
from django.conf import settings

register = template.Library()
@register.simple_tag
def mystatic(value):
    return settings.STATIC_URL+value