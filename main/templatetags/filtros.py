from django.template.defaultfilters import stringfilter
from django import template



register = template.Library()

@register.filter
@stringfilter
def calcular_clase(tipo_mensaje):
    if tipo_mensaje == 'error':
        return 'danger'
    return tipo_mensaje
    