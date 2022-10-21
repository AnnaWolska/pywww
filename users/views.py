from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from django.views.generic import ListView
from django.views.generic import TemplateView


class UserCounter(View):
    model = User
    template_name = 'counter.html'

    def get(self, request):
        users_counter = self.model.objects.count()
        return render(request, self.template_name, {'users_counter': users_counter})


user_counter = UserCounter.as_view()


# class MyDetailView(DetailView):
#     model = User


# class MyDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"

class MyDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = MyDetailView.as_view()


# class MyListView(DetailView):
#     model = User


class UserListView(ListView):
    model = User


user_list_view = UserListView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        "bio",
    ]


user_update_view = UserUpdateView.as_view()