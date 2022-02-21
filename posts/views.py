from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from posts.models import Post

# Create your views here.

class PostListView(ListView):
  template_name = "post_list.html"
  model = Post

class PostDetailView(DetailView):
  template_name = "post_detail.html"
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
  template_name = 'post_new.html'
  model = Post
  fields = ['title', 'author', 'body']

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  template_name = 'post_update.html'
  model = Post
  fields = ['title', 'body']

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  template_name = 'post_delete.html'
  model = Post
  success_url = reverse_lazy('post_list')

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user
