# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import simplejson
# Create your views here.
from django.http import HttpResponseRedirect
from feedback import app_settings
import models
from django.db.models import Count
from django.shortcuts import get_object_or_404,render_to_response
from django.core.mail import EmailMessage


@login_required
def feedback(request):
    if request.method=="POST":
        c = models.Feedback(
                feedback=request.POST.get("feedback"),
                path=request.POST.get('path'),
                )
        c.save()
        c.upvote(request.user)
        if app_settings.FEEDBACK_SEND_MAIL and app_settings.FEEDBACK_FROM:
            _dict = {
                    'feedback': c.feedback,
                    'path': c.path,
                    'user': request.user,
                    'request': request,
            }
            if app_settings.FEEDBACK_REPLY_TO_USER:
                headers={'reply-To': request.user.email}
            else:
                headers={}
            email = EmailMessage(app_settings.FEEDBACK_SUBJECT % _dict,
                    app_settings.FEEDBACK_BODY % _dict,
                    app_settings.FEEDBACK_FROM,
                    app_settings.FEEDBACK_TO,
                    headers=headers,
            )
            email.send(fail_silently=True)

    if request.is_ajax():
        return HttpResponse(simplejson.dumps({"feedback":"accepted",
            'msg': 'Bien reçu, merci de votre participation'}),mimetype="json")
    return HttpResponseRedirect(app_settings.FEEDBACK_THANKS_URL)

@login_required
def feedbacks(request):
    feedbacks = models.Feedback.objects.all()\
        .annotate(Count('votes'))\
        .order_by('-votes__count')
    return render_to_response('feedback/feedbacks.html',{'feedbacks':feedbacks})

@login_required
def upvote(request,feedback_id):
    return vote(request,feedback_id,True)

@login_required
def downvote(request,feedback_id):
    return vote(request,feedback_id,False)

@login_required
def vote(request,feedback_id, upvote):
    f = get_object_or_404(models.Feedback,id=feedback_id)
    f.upvote(request.user,upvote)
    upvote_msg='upvoted'
    if not upvote:
        upvote_msg='downvoted'
    if request.is_ajax():
        return HttpResponse(simplejson.dumps({"feedback":upvote_msg}),mimetype="json")
    return HttpResponseRedirect(app_settings.FEEDBACK_THANKS_URL)

