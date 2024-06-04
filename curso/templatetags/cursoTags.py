from django import template

register = template.Library()

@register.filter
def ProjectTitleupper(value):
    return value.upper()+"!"
