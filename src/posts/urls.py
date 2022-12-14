from django.urls import path
from .views import (
    hello_world_view,
    load_post_data_view,
    post_list_and_create,
    like_unlike_post,
)

app_name = 'posts'

urlpatterns = [
    path('', post_list_and_create, name = 'main-board'),
    path('data/<int:numPosts>/', load_post_data_view, name = 'posts-data'),
    path('like-unlike/', like_unlike_post, name='like-unlike'),
    path('hello-world/', hello_world_view, name = "hello-world"),
]