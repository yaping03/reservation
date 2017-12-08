from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变

@register.filter
def filter_multi(v1, v2):
    return v1.get(v2)[0]

@register.filter
def my_filter(v1,v2):
    return v1.get(v2)[1]
