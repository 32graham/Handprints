from .models import Profile
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/user_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileDetailView, self).dispatch(*args, **kwargs)


def reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(
        request,
        template_name='password_reset_confirm.html',
        uidb36=uidb36,
        token=token,
        post_reset_redirect=reverse('auth_login')
    )


def reset(request):
    return password_reset(
        request,
        template_name='password_reset_form.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        post_reset_redirect=reverse('auth_login')
    )
