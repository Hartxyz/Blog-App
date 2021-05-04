from django.urls import path
from .views import (
    PostListView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
    CommentCreate,
)

urlpatterns = [
    path('<int:pk>/comment/',
        CommentCreate.as_view(), name='comments'),
    path('<int:pk>/edit/',
        PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/',
        PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/',
        PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='post_list'),
]