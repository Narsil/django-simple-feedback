from django.conf.urls.defaults import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('feedback.views', 
        url(r'upvote/(?P<feedback_id>[0-9]*)$', 'upvote'), 
        url(r'downvote/(?P<feedback_id>[0-9]*)$', 'downvote'), 
        url(r'feedbacks/$', 'feedbacks'), 
        url(r'$', 'feedback'), 
)
