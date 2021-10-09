from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password

from .models import Dsuser
from .forms import RegisterFrom, LoginForm

# Create your views here.

def home(request):
    return render(request, 'index.html', {
        'name' : request.session.get('name')
    })

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterFrom
    success_url = '/'

    def form_valid(self, form):
        user = Dsuser(name=form.data.get('name'),
                      email=form.data.get('email'),
                      password=make_password(form.data.get('password'))
                      )
        user.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    
    def form_valid(self, form):
        self.request.session['name'] = form.data.get('name')
        return super().form_valid(form)
    
def logout(request):
    del request.session['name']
    return redirect('/', request)