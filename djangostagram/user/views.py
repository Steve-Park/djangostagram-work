from django.db.models.query import QuerySet
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth.hashers import make_password

from .models import DSUser
from .forms import RegisterFrom, LoginForm
from post.models import Post

# Create your views here.


class Timeline(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'timeline.html'
    paginate_by = 4

    def get_queryset(self):
        # return super().get_queryset()
        return Post.objects.order_by('-registered_date')


class RegisterUser(FormView):
    template_name = 'register_user.html'
    form_class = RegisterFrom
    success_url = '/'

    def form_valid(self, form):
        user = DSUser(name=form.data.get('name'),
                      email=form.data.get('email'),
                      password=make_password(form.data.get('password'))
                      )
        user.save()

        return super().form_valid(form)


class LoginUser(FormView):
    template_name = 'login_user.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['name'] = form.data.get('name')
        return super().form_valid(form)


def logout(request):
    del request.session['name']
    return redirect('/', request)
