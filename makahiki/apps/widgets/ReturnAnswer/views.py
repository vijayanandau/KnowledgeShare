"""Views handler for ask admin page rendering."""
from django.core.urlresolvers import reverse

import simplejson as json
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from apps.managers.challenge_mgr import challenge_mgr
from apps.widgets.ReturnAnswer.models import ReturnAnswer
from apps.widgets.ReturnAnswer.forms import AnswerForm
from apps.widgets.AskQuestion.forms import QuestionForm
from apps.widgets.AskedQuestions.forms import AskedQuestionForm
from apps.widgets.AskQuestion.models import AskQuestion

def supply(request, page_name):
    """Supply view_objects for widget rendering, returns form."""
    _ = request
    _ = page_name
    
    user = request.user
        #AskedQuestionForm.questionid= 2
    if hasattr(AskedQuestionForm,"questionid"):
        if AskedQuestionForm.questionid <> 0:
            question = AskQuestion.objects.get(id=AskedQuestionForm.questionid,)
            answers = ReturnAnswer.objects.filter(m_question_id=AskedQuestionForm.questionid,)
            currentAnswer = ReturnAnswer.objects.filter(m_question_id=AskedQuestionForm.questionid,)
            #currentAnswer = "This is a test"
        else:
            question = "" 
            answers = ""
            currentAnswer = ""   
        #test = AskedQuestionForm.questionid
        #test = "Wtf"
    else:
        question = ""
        answers = ""
        currentAnswer = "" 
    
    #answer = ReturnAnswer.objects.get(m_question_id=QuestionForm.questionid)

    return {
        #"answers":ReturnAnswer.objects.get(m_question_id=1),
        "question_p":question,
        "currentuser":user,
        "answer_p": answers,
        "currentanswer":currentAnswer#answer.m_answer,
        }


def send_answer(request):
    """send feedback."""
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            #print "email sent %s" % html_message
            user = request.user
            answer, created = ReturnAnswer.objects.get_or_create(m_user=user, m_question_id = AskedQuestionForm.questionid)
            answer.m_answer = request.POST['answer']
            answer.m_user = user
            answer.m_question_id = AskedQuestionForm.questionid
            answer.m_rating = 1
            answer.save()
            #if request.is_ajax():
            if "HTTP_REFERER" in request.META:
                return HttpResponseRedirect(request.META["HTTP_REFERER"])
            else:
                return HttpResponseRedirect(reverse("home_index"))

