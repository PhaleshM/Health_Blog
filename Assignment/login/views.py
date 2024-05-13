from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login,authenticate
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import SignUpForm,LoginForm
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth.views import LogoutView
from blog.models import Post, Comment

@login_required(login_url=reverse_lazy('login'))
def UserProfile(request):
    user=request.user
    data = User.objects.get(email=user.email)
    posts=Post.objects.filter(author=user.id)
    comments=Comment.objects.filter(user=user.id)
    context = {
        'user_data': data,
        'posts':posts,
        'comments':comments

    }
    return render(request, 'base.html', context)

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


class UserLogoutView(LogoutView):
    next_page='post_list'
