from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/blog_list.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    queryset = Blog.objects.all()
    new_comment = None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['commentForm'] = CommentForm()
        context['otherBlogs'] = Blog.objects.all().order_by('modified')
        return context

    