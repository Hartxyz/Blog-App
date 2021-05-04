from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .models import Posts, Comment
from .forms import CommentForm

class PostListView(ListView):
    model = Posts
    template_name = 'post_list.html'
    
    def get_queryset(self):
        return Posts.objects.order_by('created_on').reverse()
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model= Posts
    template_name = 'post_new.html'
    fields = ('title', 'body',)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'
    
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.posts_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ('title', 'body',)
    template_name = 'post_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user