"""Ask Admin URL."""

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^return-answer/$',
        'apps.widgets.ReturnAnswer.views.send_answer', name="return_answer"),
)
