"""Ask Admin URL."""

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^my_question/$',
        'apps.widgets.AskedQuestions.views.send_question', name="ask_que_question"),
)
