from .models import TicketComment, Ticket
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = TicketComment
        fields = ['comment']


class EditTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['tier']

class NewTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title','company','state','tier']
