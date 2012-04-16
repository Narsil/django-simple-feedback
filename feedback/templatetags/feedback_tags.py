from django.template import Library
from django.conf import settings
from feedback import app_settings

register = Library()


@register.inclusion_tag('feedback/base.html', takes_context=True)
def feedback(context):
    if 'request' in context:
        path = context['request'].path
    elif settings.DEBUG:
        raise Exception("Please include 'django.core.context_processors.request' in TEMPLATE_CONTEXT_PROCESSORS")
    else:
        path = 'path not configured'

    return {'PATH': path,
            'ASK_EMAIL': app_settings.FEEDBACK_ASK_EMAIL and not context['request'].user.email,
            'STATIC_URL': settings.STATIC_URL}
