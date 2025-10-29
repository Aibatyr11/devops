from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import UserProfile

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, "users.html", {"users": users})
