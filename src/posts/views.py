from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def post_list_and_create(request):
    qs = Post.objects.all()
    return render(request, 'posts/main.html', {'qs': qs})

def load_post_data_view(request, numPosts):
    # num_posts   = kwargs.get('num_posts') adding kwargs as an entry for load_post_data_view would be another option
    visible = 3
    upper = numPosts
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    #data = serializers.serialize('json',qs)
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'body': obj.body,
            'liked': True if request.user in obj.liked.all() else False,
            'count': obj.like_count,
            'author': obj.author.user.username
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size': size})

def like_unlike_post(request):
    #if request.is_ajax():
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked': liked, 'count': obj.like_count})

def hello_world_view(request):
    return JsonResponse({'text': 'hello world!!!'})
