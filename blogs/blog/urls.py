from django.urls import path

from .views import ListViewOfBlog, DetailViewofBlog, NewBlogPost, EditBlogPost

urlpatterns = [

    path('post/edit/<int:pk>/', EditBlogPost.as_view(), name='post_edit'),

    path('post/new/', NewBlogPost.as_view(), name="new_post"),
    path('post/<int:pk>/', DetailViewofBlog.as_view(),
         name='detailed_post'),



    path('', ListViewOfBlog.as_view(), name='home'),


]
