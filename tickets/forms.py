from .models import TicketComment, Ticket
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = TicketComment
        fields = ['comment', 'attachment',]



class EditTicketForm(forms.ModelForm):

    class Meta:
        fields = ['tier', 'status',]
        model = Ticket


class NewTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'company',
            'tier',
            'status'
        ]
