from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User


class UserCounter(View):
    model = User
    template_name = 'counter.html'

    def get(self, request):
        users_counter = self.model.objects.count()
        return render (request, self.template_name, {'users_counter':users_counter})


user_counter = UserCounter.as_view()

