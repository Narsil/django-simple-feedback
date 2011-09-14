=====================================
django-simple-feedback (django-simple-feedback)
=====================================

This `Django<http://djangoproject.com>`_ app has for purpose to integrate easily user based feedback.
It aims to be easily added into existing projects and pretty on any website.

NEW in master
~~~~~~~~~~~~~
master version is now operational for Django-1.3 with `collectstatic <https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#collectstatic>`_
This will break backward compatibility, branch django-1.2.5 is the last working
state for Django-1.2.5

Installation 
============

Depedencies  
~~~~~~~~~~~

django-simple-feedback requires jQuery, and it includes it in its static files.

Installing django-simple-feedback
~~~~~~~~~~~~~~~~~~~~~~~~~~

Install into your python path using pip or github version::

    pip install django-simple-feedback
    pip install -e git://github.com/Narsil/django-simple-feedback

Add *'feedback'* to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'feedback',
    )

Add css and javascript in your *'base.html'* template (jQuery is optional if you already include it in your project)::

    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}feedback/css/feedback.css" />

    <script type="text/javascript" src="{{ STATIC_URL }}feedback/js/jquery-1.4.2.min.js"></script>
    <script type="text/javascript" src="{{ STATIC_URL }}feedback/js/feedback.js"></script>

And then in templates where you want feedback to appear::

    {% load feedback_tags %}
    ....

    {% feedback %}

Add *'(r'^feedback', include('feedback.urls')'* to your urls:: 

    urlpatterns = patterns( '',
        ....
        (r'^feedback', include('feedback.urls'),
    )

Don't forget to run ::

    ./manage.py syncdb
        
to create the table that is going to receive the feedbacks.

Receiving mail of feedbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you wish to receive mail when someone posts some feedback then you need to
configure these which are the defaults::

    FEEDBACK_SEND_MAIL = True
    FEEDBACK_FROM = 'feedback@example.com'
    FEEDBACK_TO = map(lambda x:x[1], settings.MANAGERS) (should be managers emails)
    FEEDBACK_SUBJECT = '[feedback] %(path)s'
    FEEDBACK_BODY = '%(feedback)s'

In `FEEDBACK_SUBJECT` and `FEEDBACK_BODY` you are able to customize the text.
each string is formatted with a dict containing the path on which the feedback
was made and the core of the message
