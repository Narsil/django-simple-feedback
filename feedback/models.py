from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.

class Feedback(models.Model):
    feedback = models.CharField(max_length=1000,blank=True,null=True)
    user = models.ForeignKey(auth_models.User)

    def __unicode__(self):
        return str(self.feedback)
