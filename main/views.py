from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from main.forms import ContactForm, UserProfileForm
from . import services
from django.contrib.auth import get_user_model


def hello_world(request):
    return render(request, 'main/about.html')


def my_tests(request):
    hello = "Hello Word"
    some_number = 999
    some_dict = {
        "cat" : "miau",
        "dog" : "hau",
        "hors" : "iha"
    }
    return render(request, 'main/tests.html', context = {
        'hello' : hello,
        'some_number' : some_number,
        'some_dict' : some_dict
    })


def home_view(request):
    return render(request, 'main/home.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            services.send_message(form.cleaned_data)
            return HttpResponseRedirect(reverse("main:contact"))
    else:
        form = ContactForm()
    return render(request, "main/contact.html", {"form":form})


def user_profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if request.method == "POST":
        try:
            profile = user.userprofile
            form = UserProfileForm(request.POST, instance=profile)
        except AttributeError: pass
        if form.is_valid(): form.save()
    else:
        try:
            profile = user.userprofile
            form = UserProfileForm(instance=profile)
        except AttributeError:
            form = UserProfileForm(initial={"user": user, "bio": ""})
        if request.user != user:
            for field in form.fields:
                form.fields[field].disabled = True
            form.helper.inputs = []
    return render(request, 'main/userprofile.html', {'form':form})