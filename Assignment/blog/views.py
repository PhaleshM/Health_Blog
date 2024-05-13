from django.views.generic import ListView, CreateView, UpdateView, DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.postobjects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query) |  Q(category__name__icontains=query)
            )
        return queryset

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    login_url = '/login/'
    success_url='/'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    login_url = '/login/'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        raise PermissionDenied("You are not allowed to update this post.")

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'  # Redirect to home after deletion
    template_name = 'post_confirm_delete.html'
    login_url = '/login/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        raise PermissionDenied("You are not allowed to Delete this post.")
    
@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': form})

class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('post_list')

    def get_success_url(self):
        return self.success_url

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user) | queryset.filter(post__author=self.request.user)