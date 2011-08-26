from django.template import Library
from django.conf import settings
from django.core.urlresolvers import reverse

register = Library()

@register.inclusion_tag('feedback/base.html')
def feedback(path=''):
    return {'PATH': path,
            'STATIC_URL': settings.STATIC_URL}

@register.inclusion_tag('feedback/scripts.html')
def feedback_scripts():
    return {'STATIC_URL': settings.STATIC_URL}
