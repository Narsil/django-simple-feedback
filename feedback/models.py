from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.

        

class Vote(models.Model):
    feedback = models.ForeignKey('Feedback',related_name='votes')
    user = models.ForeignKey(auth_models.User)
    vote = models.BooleanField()
    

    def __unicode__(self):
        return str(self.feedback)

class Feedback(models.Model):
    feedback = models.CharField(max_length=1000,blank=True,null=True)

    def upvote(self,user,upvote=True):
        vote = Vote(feedback=self,user=user,vote=upvote)
        vote.save()


    def __unicode__(self):
        if not self.votes.all():
            return self.feedback
        votes = map(lambda x: x.vote,self.votes.all())
        upvotes = sum(votes)
        downvotes = len(votes)-upvotes
        return "%s (%i/%i)"%(self.feedback,upvotes,downvotes)
