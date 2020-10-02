import os
from django.urls import reverse
from articles.db_getters import *
from articles.exceptions import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import AuthWithRememberingSession
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import logout, login, authenticate
from articles.base import BlogBaseContextMixin, BaseBlogView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# dir where will be stored all registration templates
REGISTRATION_DIR = "registration"


class MyLoginView(BlogBaseContextMixin, LoginView):
    #form should have field 'remember_me'
    #if form have not remove post function in this class
    form_class = AuthWithRememberingSession
    success_redirect_name = 'accounts:success_login'
    template_name = os.path.join(REGISTRATION_DIR, 'login.html')

    def get_redirect_url(self):
        return reverse(self.success_redirect_name)

    def post(self, request, *args, **kwargs):
        print('this is post function in LOGINVIEW and request.POST = ' + str(request.POST))
        if request.POST.get('remember_me', 'No') == 'No':
            #if user dont ask to remember him
            # close session when browser will be ended
            request.session.set_expiry(0)
        return super().post(request, *args, **kwargs)


class MySuccessLoginView(BaseBlogView):
    template_name = os.path.join(REGISTRATION_DIR, 'success_login.html')


class MyLogoutView(BaseBlogView, LogoutView):
    next_page = 'articles:base_page'


class MyRegistrationView(BaseBlogView):
    template_name = os.path.join(REGISTRATION_DIR, 'registration_form.html')
    success_url = 'success_login/' #  reverse('accounts:success_registration')
    extra_context = {
        'create_user_form': UserCreationForm(),
    }

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            self.extra_context['create_user_form'] = form
            return self.render_to_response(self.get_context_data(**kwargs))


class MySuccessRegistrationView(BaseBlogView):
    template_name = os.path.join(REGISTRATION_DIR, 'registration_complete.html')


def registrate(request):
    menu = getMenu()
    footer = getFooter()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        registration_form_template_path = os.path.join(REGISTRATION_DIR, 'registration_form.html')
        registration_complete_template_path = os.path.join(REGISTRATION_DIR, 'registration_complete.html')
        if form.is_valid():
            form.save()
            return render(request, registration_complete_template_path, {'menu': menu,
                                                                         'footer': footer})
        else:
            return render(request, registration_form_template_path, {'create_user_form': form,
                                                                     'menu': menu,
                                                                     'footer': footer})
    else:
        registration_form_template_path = os.path.join(REGISTRATION_DIR, 'registration_form.html')
        userCreationForm = UserCreationForm()
        return render(request, registration_form_template_path, {'create_user_form': userCreationForm,
                                                                        'menu': menu,
                                                                        'footer': footer})

def log_in(request):
    menu = getMenu()
    footer = getFooter()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'registration\\success_login.html', {'menu': menu,
                                                                        'footer': footer})
        else:
            error = 'There is no user with such password and name'
            return render(request, 'registration\\login.html', {'menu': menu,
                                                                'footer': footer,
                                                                'form': form,
                                                                'errors': error})
    else:
        form = AuthenticationForm()
        return render(request, 'registration\\login.html', {'menu': menu,
                                                            'footer': footer,
                                                            'form': form})
# Create your views here.
