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


class ViewPost(DetailView):
    template_name = 'view_post.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm(self.request)
        return context

    # def get_queryset(self):
    #     # return super().get_queryset()
    #     self.pk = get_object_or_404(Post, pk=self.kwargs['pk'])
    #     return Post.objects.get(pk=self.pk)
