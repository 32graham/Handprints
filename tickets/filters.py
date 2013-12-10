import django_filters
from .models import Ticket
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from django.core.urlresolvers import reverse


class TicketFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = ['tier', 'status', 'tier__department', 'product']

    def __init__(self, *args, **kwargs):
        super(TicketFilter, self).__init__(*args, **kwargs)
        self.form.helper = FormHelper()
        self.form.helper.form_action = reverse('tickets')
        self.form.helper.form_method = 'get'
        self.form.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Div('tier', css_class='col-sm-6'),
                    Div('status', css_class='col-sm-6'),
                    css_class='row'
                ),
                Div(
                    Div('tier__department', css_class='col-sm-6'),
                    Div('product', css_class='col-sm-6'),
                    css_class='row'
                )
            ),
            ButtonHolder(
                Submit('', 'Filter', css_class='btn-primary')
            )
        )

