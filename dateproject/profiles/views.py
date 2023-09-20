from django.shortcuts import render
from profiles.models import UserProfile


# Create your views here.
def show_profiles(request):
    context = {"profiles": UserProfile.objects.all(),
               "choices": dict(UserProfile.STATUS)}
    return render(request, "profiles.html",
                  context=context)


def show_profile(request, profile):
    context = {"profile": UserProfile.objects.get(pk=profile)}
    return render(request,
                  "profile.html",
                  context=context)
