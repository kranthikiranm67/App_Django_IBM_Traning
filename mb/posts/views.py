from django.shortcuts import render

from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_items'

    # i want the data form the post model to be present
    # on the home.html page

# Create your views here.
