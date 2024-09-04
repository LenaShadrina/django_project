from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from . import models, forms

# Create your views here.


class MyLoginView(auth_views.LoginView):
    template_name = "acc/login.html"
    success_url = reverse_lazy("accounts:profile-detail")


def logout_view(request):
    logout(request)
    return redirect('/catalog')

def login_view(request):
    if request.method == "GET":
        return_to = request.GET.get('next')
        context = {'return_to': return_to}
        return render(request, 'acc/login.html', context)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        redirect_to = request.POST.get("next", "/")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("accounts:profile-detail"))
        else:
            context = {
                'error_ message': 'Username or/and password are incorrect',
                'username': username
            }
            return render(request, 'acc/login.html', context)


class CheckProfileMixin(LoginRequiredMixin):
    redirect_on_missing_profile = True

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(
            user__pk=user.pk
        )
        redirect_needed = bool(profile)
        if self.redirect_on_missing_profile == True:
            redirect_needed = not redirect_needed
        if redirect_needed:
            return HttpResponseRedirect(self.profile_redirect_url)
        return super().dispatch(request, *args, **kwargs)


class CustomerProfileCreate(CheckProfileMixin, generic.CreateView):
    profile_redirect_url = reverse_lazy("accounts:profile-detail")
    redirect_on_missing_profile = False
    model = models.CustomerProfile
    template_name = "acc/profile_create.html"
    form_class = forms.ProfileCreateForm
    success_url = reverse_lazy("accounts:profile-detail")

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        self.object = profile
        return HttpResponseRedirect(self.get_success_url())


class CustomerProfileDetail(CheckProfileMixin, generic.DetailView):
    profile_redirect_url = reverse_lazy("accounts:profile-create")
    redirect_on_missing_profile = True
    template_name = "acc/profile.html"


    def get_object(self):
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(
            user__pk=user.pk
        )

        if profile:
            profile = profile[0]
        else:
            profile = models.CustomerProfile.objects.create(
               user=user,
               description="pls fill in"
           )
        return profile
