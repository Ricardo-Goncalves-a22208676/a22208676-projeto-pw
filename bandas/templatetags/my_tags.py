from django import template

register = template.Library()

@register.filter
def upper(value):
    return value.upper()

# Para usar a sua custom tag nos seus templates
#{% load my_tags %}
#<h1>{{ banda.nome|upper }}</h1>