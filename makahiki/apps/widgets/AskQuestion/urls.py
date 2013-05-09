"""Ask Admin URL."""

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^ask-question/$',
        'apps.widgets.AskQuestion.views.ask_question', name="ask_que_q"),
)
