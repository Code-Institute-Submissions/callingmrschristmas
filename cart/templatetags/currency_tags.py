from django import template

register = template.Library()

@register.simple_tag
def currency(value):
    """Custom template tag for displaying currency"""
    value_decimal = value / 100
    currency_string = "£ " + str(value_decimal)
    return currency_string
