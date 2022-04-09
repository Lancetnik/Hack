from django.urls import path

from . import views


urlpatterns = (
    path('position/<int:pk>/', views.GetPostition.as_view()),
)
