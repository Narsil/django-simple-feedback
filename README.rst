=====================================
django-simple-feedback (django-simple-feedback)
=====================================

This Django_ app has for purpose to integrate easily user based feedback.
It aims to be easily added into existing projects and pretty on any website.

Installation 
============

Depedencies  
~~~~~~~~~~~

django-simple-feedback requires jQuery, and it includes it in noConflict mode.

Installing django-simple-feedback
~~~~~~~~~~~~~~~~~~~~~~~~~~

Install into your python path using pip or easy_install::

    pip install django-simple-feedback
    easy_install django-simple-feedback

Add *'feedback'* to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'feedback',
    )

Add *'feedback.middleware.FeedbackMiddleware'* to you MIDDLEWARE_CLASSES::

    MIDDLEWARE_CLASSES = (
        ...
        'feedback.middleware.FeedbackMiddleware',
    )

Add *'(r'^', include('feedback.urls')'* to your urls:: 

    urlpatterns = patterns( '',
        ....
        (r'^', include('feedback.urls'),
    )

Don't forget to run ::

    ./manage.py syncdb
        
to create the table that is going to receive the feedbacks.

Modifying urls for django-simple-feedback  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can if you wish modify the urls for django-simple-feedback by adding:: 

    FEEDBACK_PREFIX = 'mynewfeedbackprefix'

Changing the number of top feedbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Top feedbacks can be changed with the settings::

    TOP_FEEDBACKS_COUNT = {0,1,2}
