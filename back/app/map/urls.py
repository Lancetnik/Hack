from django.urls import path

from . import views


urlpatterns = (
    path('single-file/', views.GetLocation.as_view()),
)
