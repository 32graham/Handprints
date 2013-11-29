from .models import TicketComment, Ticket, Product
from profiles.models import Profile
from django import forms
from django_select2.widgets import Select2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from django.core.urlresolvers import reverse


class StaffCommentForm(forms.ModelForm):

    class Meta:
        model = TicketComment
        fields = ['comment', 'is_public', 'attachment',]


class StandardCommentForm(StaffCommentForm):

    class Meta(StaffCommentForm.Meta):
        exclude = ('is_public')


class EditTicketForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.order_by('name'), required=False)

    class Meta:
        widgets = {
            'assignees': Select2MultipleWidget(select2_options={'closeOnSelect': True})
        }
        fields = ['tier', 'status', 'assignees', 'product',]
        model = Ticket

    def __init__(self, *args, **kwargs):
        super(EditTicketForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('ticket', args=[self.instance.pk])
        self.helper.layout = Layout(
            Fieldset(
                '',
                'product',
                'tier',
                'status',
                Field('assignees', css_class='col-xs-12'),
            ),
            ButtonHolder(
                Submit('ticket_post', 'Save', css_class='btn-warning')
            )
        )
        self.fields['assignees'].help_text = ''
        self.fields['assignees'].queryset = Profile.objects.filter(user__is_staff=True)


class NewTicketForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.order_by('name'), required=False)

    class Meta:
        widgets = {
            'assignees': Select2MultipleWidget(select2_options={'closeOnSelect': True})
        }
        fields = [
            'title',
            'description',
            'product',
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
                'product',
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
        self.fields['assignees'].queryset = Profile.objects.filter(user__is_staff=True)
