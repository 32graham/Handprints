from .models import TicketComment, Ticket
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = TicketComment
        fields = ['comment']



class EditTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['assignee', 'is_blocker', 'tier', 'status']


class NewTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'company',
            'assignee',
            'tier',
            'status',
            'is_blocker',
        ]
