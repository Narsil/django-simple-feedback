from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
import settings

_PREFIX = getattr(settings, 'FEEDBACK_PREFIX' ,'__feedback__')

urlpatterns = patterns('',
        (r'^%s/$' % _PREFIX,'feedback.views.feedback'),
        (r'^%s/media/(.*)$' %_PREFIX,'feedback.views.feedback_media'),
)
