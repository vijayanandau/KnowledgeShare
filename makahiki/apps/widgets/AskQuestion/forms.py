"""Provides a simple text area for users to type their question to the admin."""

from django import forms


class QuestionForm(forms.Form):
    """Ask Admin feedback form."""
    url = forms.URLField(required=False, widget=forms.HiddenInput)
    question = forms.CharField(widget=forms.Textarea())
    #questionid = forms.IntegerField(required=False, widget=forms.HiddenInput)

