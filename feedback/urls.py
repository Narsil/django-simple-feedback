from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
import settings

PREFIX = getattr(settings, 'FEEDBACK_PREFIX' ,'__feedback__')
_PREFIX = "/%s" %PREFIX

urlpatterns = patterns('',
        (r'^%s/$' % PREFIX,'feedback.views.feedback'),
        (r'^%s/media/(.*)$' %PREFIX,'feedback.views.feedback_media'),
)
