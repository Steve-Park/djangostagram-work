from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404

from .forms import PostForm
from .models import Tag, Post
from user.models import DSUser

# Create your views here.


class UploadPost(FormView):
    template_name = 'upload_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        author = DSUser.objects.get(name=self.request.session.get('name'))

        post = Post(title=form.data.get('title'),
                    content=form.data.get('content'),
                    imageurl=form.data.get('imageurl'),
                    author=author)
        post.save()

        for tag_name in form.data.get('tags').split(','):
            tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
            post.tags.add(tag)

        return super().form_valid(form)


class ViewPost(FormView, DetailView):
    model = Post
    form_class = PostForm
    template_name = 'view_post.html'
    context_object_name = 'post'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        return FormView.post(self, request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(pk=self.kwargs['pk'])

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])

        post.title = form.data.get('title')
        post.content = form.data.get('content')
        post.imageurl = form.data.get('imageurl')
        post.save()

        post.tags.clear()

        for tag_name in form.data.get('tags').split(','):
            tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
            post.tags.add(tag)

        return super().form_valid(form)
