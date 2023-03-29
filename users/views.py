from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
# from main.models import UserProfile
from django.views.generic import DetailView, UpdateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import  SuccessMessageMixin


class UserCounter(View):
    model = User
    template_name = 'counter.html'

    def get(self, request):
        users_counter = self.model.objects.count()
        return render(request, self.template_name, {'users_counter': users_counter})


user_counter = UserCounter.as_view()


class MyDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    slug_field = "username"
    slug_url_kwarg = "username"
    success_url = '/success'
    success_message = "Thi is details for %(username)"


user_detail_view = MyDetailView.as_view()


class UserListView(ListView):
    model = User
    template_name = "user_list.html"
    # success_message = _("Profile actualized")


user_list_view = UserListView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        # "bio",
    ]
    model = User
    template_name = "user_form.html"

    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
        return User.objects.get(
            username=self.request.user.username
        )


user_update_view = UserUpdateView.as_view()
