"""action_feedback model."""

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from apps.widgets.smartgrid.models import Action
from apps.managers.challenge_mgr import challenge_mgr
from apps.admin.admin import challenge_designer_site, challenge_manager_site, developer_site


class AskQuestion(models.Model):
    """Defines the Action Feedback model."""
    m_question = models.CharField(max_length=8000)
    m_user = models.ForeignKey(User,
                             null=True, blank=True,
                             help_text="The user asking the question.")
    m_isopen = models.BooleanField()
    
    def __unicode__(self):
        return "%s rated %s %d and said %s" % \
            (self.user.username, self.action.name, self.rating, self.comment)

admin.site.register(AskQuestion)
challenge_designer_site.register(AskQuestion)
challenge_manager_site.register(AskQuestion)
developer_site.register(AskQuestion)
#challenge_mgr.register_developer_game_info_model("Smart Grid Game", ActionFeedback)
