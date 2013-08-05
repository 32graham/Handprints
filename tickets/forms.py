from .models import TicketComment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = TicketComment
        fields = ['comment']
