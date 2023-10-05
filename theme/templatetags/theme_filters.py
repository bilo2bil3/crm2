from django import template
from crispy_tailwind.templatetags.tailwind_filters import as_crispy_form

register = template.Library()

@register.filter(name='custom_crispy_form')
def custom_crispy_form(form, style):
    return as_crispy_form(form, label_class=style)