from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import simplejson
# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
import django.views.static
import models


@login_required
def feedback(request):
    if request.method=="POST":
        c = models.Feedback(
                feedback=request.POST.get("feedback"))
        c.save()
        c.upvote(request.user)
    #return HttpResponseRedirect(reverse('main.views.index'))
    if request.is_ajax():
        return HttpResponse(simplejson.dumps({"feedback":"accepted"}),mimetype="json")
    return HttpResponseRedirect(reverse('main.views.index'))

@login_required
def upvote(request,feedback_id, upvote):
    f = get_object_or_404(Feedback,id=feedback_id)
    f.upvote(request.user,upvote)
    upvote_msg='upvoted'
    if not upvote:
        upvote_msg='downvoted'
    if request.is_ajax():
        return HttpResponse(simplejson.dumps({"feedback":upvote_msg}),mimetype="json")
    return HttpResponseRedirect(reverse('main.views.index'))

def feedback_media(request, path):
    parent = os.path.abspath(os.path.dirname(__file__))
    root = os.path.join(parent, 'media')
    return django.views.static.serve(request, path, root)
