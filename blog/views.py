from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import views as auth_views

# Create your views here.
def post_list(request):
    if request.user.is_authenticated():
        posts = Post.objects.filter(author=request.user).filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'floathub/base.html', {'posts': posts})
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return auth_views.login(request)


def post_new(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('/notes/', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'floathub/post_edit.html', {'form': form})
    return auth_views.login(request)

def login(request):
    return auth_views.login(request)

def home(request):
    return render(request, 'floathub/index.html', {})

def delete_post(request,id):
   u = Post.objects.get(pk=id).delete()
   posts = Post.objects.filter(author=request.user).filter(published_date__lte=timezone.now()).order_by('-published_date')
   return render(request, 'floathub/base.html', {'posts': posts})

def edit_post(request,id):
    u = Post.objects.get(pk=id)

    if request.user.is_authenticated():
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                u.delete()
                return redirect('/notes/', pk=post.pk)


    form = PostForm(instance=u)

    return render(request, 'floathub/edit.html', {'form': form, 'u': u})
