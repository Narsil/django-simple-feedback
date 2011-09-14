from models import Feedback, Vote
from django.contrib import admin


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0


class FeedbackAdmin(admin.ModelAdmin):
    inlines = (VoteInline,)
    list_display = ('feedback', 'path', 'upvotes', 'downvotes')


admin.site.register(Feedback, FeedbackAdmin)
