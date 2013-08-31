from .models import TicketComment, Ticket
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = TicketComment
        fields = ['comment']


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['tier']
