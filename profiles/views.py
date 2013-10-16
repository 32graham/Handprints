from django.contrib.auth.models import User
from django.views.generic import DetailView


class ProfileDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'profiles/user_detail.html'
