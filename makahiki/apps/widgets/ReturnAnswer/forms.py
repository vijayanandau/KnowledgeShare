"""Provides a simple text area for users to type their question to the admin."""

from django import forms


class AnswerForm(forms.Form):
    """Ask Admin feedback form."""
    url = forms.URLField(required=False, widget=forms.HiddenInput)
    answer = forms.CharField(widget=forms.Textarea())


