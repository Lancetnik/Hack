from django.urls import path

from .views import FindUsersView


urlpatterns = [
    path('find/', FindUsersView.as_view()),
]