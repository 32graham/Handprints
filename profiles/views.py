from django.shortcuts import render
from django.contrib.auth.models import User


def profile(request, user_id):
    user = User.objects.get(pk=user_id)

    return render(
        request,
        'profiles/profile.html',
        {'user': user}
    )
