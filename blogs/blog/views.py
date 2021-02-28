from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView

from .models import Post


class ListViewOfBlog(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'


class DetailViewofBlog(DetailView):
    model = Post
    template_name = 'detailed_post.html'


class NewBlogPost(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']


class EditBlogPost(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    # Create your views here.
