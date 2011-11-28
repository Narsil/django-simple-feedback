from django.db import models
from django.contrib.auth import models as auth_models
from math import sqrt
# Create your models here.


class Vote(models.Model):
    feedback = models.ForeignKey('Feedback',related_name='votes')
    user = models.ForeignKey(auth_models.User)
    vote = models.BooleanField()
    

    def __unicode__(self):
        return str(self.feedback)

class Feedback(models.Model):
    feedback = models.CharField(max_length=1000,blank=True,null=True)
    path = models.CharField(max_length=256,blank=True,null=True)

    def upvote(self,user,upvote=True):
        vote = Vote(feedback=self,user=user,vote=upvote)
        vote.save()

    def score(self):
        votes = map(lambda x:x.vote,self.votes.all())
        ups = sum(votes)
        n = len(votes)
        downs = n - ups
        return ups-downs

    def confidence(self):
        if not self.votes:
            return 0
        votes = map(lambda x:x.vote,self.votes.all())
        ups = sum(votes)
        n = len(votes)

        if n == 0:
            return 0

        z = 1.0 #1.0 = 85%, 1.6 = 95%
        phat = float(ups) / n
        return sqrt(phat+z*z/(2*n)-z*((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n)

    def upvotes(self):
        return self.votes.filter(vote=True).count()

    def downvotes(self):
        return self.votes.filter(vote=False).count()

    def __unicode__(self):
        if not self.votes.all():
            return self.feedback
        votes = map(lambda x: x.vote,self.votes.all())
        upvotes = sum(votes)
        downvotes = len(votes)-upvotes
        return "%s (%i/%i)"%(self.feedback,upvotes,downvotes)
