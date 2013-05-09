"""Views handler for ask admin page rendering."""
from django.core.urlresolvers import reverse

import simplejson as json

from django.http import Http404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from apps.managers.challenge_mgr import challenge_mgr
from apps.widgets.AskQuestion.models import AskQuestion
from apps.widgets.AskedQuestions.forms import AskedQuestionForm
from apps.widgets.AskQuestion.forms import QuestionForm


def supply(request, page_name):
    """Supply view_objects for widget rendering, returns form."""
    _ = request
    _ = page_name
    
    user = request.user
    #AskedQuestionForm.questionid= 2
    if hasattr(AskedQuestionForm,"questionid"):
        if AskedQuestionForm.questionid <> 0:
            question = AskQuestion.objects.get(id=AskedQuestionForm.questionid,)
        else:
            question = ""    
        #test = AskedQuestionForm.questionid
        #test = "Wtf"
    else:
        question = ""
        #test = "fail"
    
       
    #QuestionForm.questionid = question.id
    return {
         "question_p":question,
         "currentuser":user,
         #"test":test
         #"question_id": question.id,
        }

def ask_question(request):
    """send feedback."""
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            #print "email sent %s" % html_message
            user = request.user
            isopen = True
            #question, created = AskQuestion.objects.get_or_create(m_user=user)
            if hasattr(AskedQuestionForm,"questionid"):
                if AskedQuestionForm.questionid == 0:
                    question = AskQuestion.objects.create()
                else:   
                    question, created = AskQuestion.objects.get_or_create(id=AskedQuestionForm.questionid,)
                    if  'question-close-button' in request.POST:
                        isopen = False
                        
            else:        
                question = AskQuestion.objects.create()
  
            
            question.m_question = request.POST['question']
            question.m_user = user
            question.m_isopen = isopen
            question.save()
            AskedQuestionForm.questionid = 0
            
            if "HTTP_REFERER" in request.META:
                return HttpResponseRedirect(request.META["HTTP_REFERER"])
            else:
                return HttpResponseRedirect(reverse("home_index"))
        #else:    
        #    raise Http404
