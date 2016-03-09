from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.order_by('published_date')
	posts_count = Post.objects.count()
	return render(request, 'blog/post_list.html',{'posts':posts,'posts_count':posts_count})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})
