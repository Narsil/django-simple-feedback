from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
import settings

PREFIX = getattr(settings, 'FEEDBACK_PREFIX' ,'__feedback__')
_PREFIX = "/%s" %PREFIX

urlpatterns = patterns('',
        url(r'^%s/upvote/(?P<feedback_id>[0-9]*)$' %PREFIX, 'feedback.views.upvote'),
        url(r'^%s/downvote/(?P<feedback_id>[0-9]*)$' % PREFIX, 'feedback.views.downvote'),
        (r'^%s/feedbacks/$' % PREFIX, 'feedback.views.feedbacks'),
        (r'^%s/$' % PREFIX,'feedback.views.feedback'),
        (r'^%s/media/(.*)$' %PREFIX,'feedback.views.feedback_media'),
)
