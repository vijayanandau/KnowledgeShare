"""Provides the view of the widget."""
from django.core.urlresolvers import reverse
from django.db.models import Q
import simplejson as json

from django.http import Http404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from apps.managers.challenge_mgr import challenge_mgr
from apps.widgets.AskQuestion.models import AskQuestion
from apps.widgets.AskedQuestions.forms import AskedQuestionForm

def supply(request, page_name):
    """ supply view_objects for widget rendering."""
    _ = request
    _ = page_name
    user = request.user
    question = AskQuestion.objects.all().filter(m_user=user,)
    openquestion = AskQuestion.objects.all().filter(m_isopen=True).filter(~Q(m_user=user))
    closedquestion = AskQuestion.objects.all().filter(m_isopen=False).filter(~Q(m_user=user))
    return {
          "question_p":question,
          "question_o":openquestion,
          "question_c":closedquestion,
    }

def send_question(request):
    """send feedback."""
    if request.method == "POST":
        form = AskedQuestionForm(request.POST)
        if form.is_valid():
            #print "email sent %s" % html_message
            user = request.user
            AskedQuestionForm.questionid = request.POST['question-id']
            #question, created = AskQuestion.objects.get_or_create(m_user=user)
            #question.m_question = request.POST['question']
            #question.m_user = user
            #question.save()
            if "HTTP_REFERER" in request.META:
                return HttpResponseRedirect(request.META["HTTP_REFERER"])
            else:
                return HttpResponseRedirect(reverse("home_index"))
    