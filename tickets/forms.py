from .models import TicketComment, Ticket
from django import forms
from django_select2.widgets import Select2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from django.core.urlresolvers import reverse


class CommentForm(forms.ModelForm):

    class Meta:
        model = TicketComment
        fields = ['comment', 'attachment',]



class EditTicketForm(forms.ModelForm):

    class Meta:
        widgets = {
            'assignees': Select2MultipleWidget(select2_options={'closeOnSelect': True})
        }
        fields = ['tier', 'status', 'assignees',]
        model = Ticket

    def __init__(self, *args, **kwargs):
        super(EditTicketForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('ticket', args=[self.instance.pk])
        self.helper.layout = Layout(
            Fieldset(
                '',
                'tier',
                'status',
                Field('assignees', css_class='col-sm-12'),
            ),
            ButtonHolder(
                Submit('ticket_post', 'Save', css_class='btn-warning')
            )
        )
        self.fields['assignees'].help_text = ''


class NewTicketForm(forms.ModelForm):

    class Meta:
        widgets = {
            'assignees': Select2MultipleWidget(select2_options={'closeOnSelect': True})
        }
        fields = [
            'title',
            'description',
            'company',
            'tier',
            'status',
            'assignees',
        ]
        model = Ticket

    def __init__(self, *args, **kwargs):
        super(NewTicketForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('new_ticket')
        self.helper.layout = Layout(
            Fieldset(
                '',
                'title',
                'description',
                'company',
                'tier',
                'status',
                Field('assignees', css_class='col-sm-12'),
            ),
            ButtonHolder(
                Submit('new_ticket', 'Save', css_class='btn-primary')
            )
        )
        self.fields['assignees'].help_text = ''
