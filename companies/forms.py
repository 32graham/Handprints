from django import forms
from .models import Company
from django_select2.widgets import Select2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset, Field, Div
from django.core.urlresolvers import reverse


class CompanyForm(forms.ModelForm):
    class Meta:
        widgets = {
            'product_versions': Select2MultipleWidget(select2_options={'closeOnSelect': True})
        }
        fields = ['notes', 'product_versions',]
        model = Company

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('company', args=[self.instance.pk])
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('product_versions', css_class='col-xs-12'),
                'notes',
            ),
            ButtonHolder(
                Submit('company_post', 'Save', css_class='btn-warning')
            )
        )
        self.fields['product_versions'].help_text = ''
