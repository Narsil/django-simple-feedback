from django.template import Library
from django.conf import settings

register = Library()


@register.inclusion_tag('feedback/base.html')
def feedback(path=''):
    return {'PATH': path,
            'STATIC_URL': settings.STATIC_URL}
