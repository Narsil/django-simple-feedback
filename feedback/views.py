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
                user=request.user,
                feedback=request.POST.get("feedback"))
        c.save()
    #return HttpResponseRedirect(reverse('main.views.index'))
    if request.is_ajax():
        return HttpResponse(simplejson.dumps({"feedback":"accepted"}),mimetype="json")
    return HttpResponseRedirect(reverse('main.views.index'))

def feedback_media(request, path):
    parent = os.path.abspath(os.path.dirname(__file__))
    root = os.path.join(parent, 'media')
    return django.views.static.serve(request, path, root)
