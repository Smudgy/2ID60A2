from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(author=request.user).filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'floathub/base.html', {'posts': posts})

def post_new(request):
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

def home(request):
    return render(request, 'floathub/index.html', {})
