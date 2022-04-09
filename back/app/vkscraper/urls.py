from django.urls import path

from . import views


urlpatterns = [
    path('user', views.FindUser.as_view()),
    path('posts/<int:user_id>', views.GetUserPosts.as_view()),
    path('posts/<int:user_id>/delay', views.GetUserPostsBackground.as_view()),
]
