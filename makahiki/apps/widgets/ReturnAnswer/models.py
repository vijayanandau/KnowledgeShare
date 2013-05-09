"""action_feedback model."""

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from apps.widgets.smartgrid.models import Action
from apps.managers.challenge_mgr import challenge_mgr
from apps.admin.admin import challenge_designer_site, challenge_manager_site, developer_site
from apps.widgets.AskQuestion.models import AskQuestion


class ReturnAnswer(models.Model):
    """Defines the Action Feedback model."""
    m_question = models.ForeignKey(AskQuestion,
                             null=True, blank=True,
                             help_text="The user asking the question.")
    m_answer = models.CharField(max_length=8000)
    m_user = models.ForeignKey(User,
                             null=True, blank=True,
                             help_text="The user answering the question.")
    m_rating = models.IntegerField(null=True,default=1)
    
    def __unicode__(self):
        return "%s rated %s %d and said %s" % \
            (self.user.username, self.action.name, self.rating, self.comment)

admin.site.register(ReturnAnswer)
challenge_designer_site.register(ReturnAnswer)
challenge_manager_site.register(ReturnAnswer)
developer_site.register(ReturnAnswer)
#challenge_mgr.register_developer_game_info_model("Smart Grid Game", ActionFeedback)
