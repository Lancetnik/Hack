from django.urls import path

from . import views


urlpatterns = (
    path('position/', views.GetPostition.as_view()),
)