from django.urls import path

from . import views


urlpatterns = [
    path('find/', views.FindUsersView.as_view()),
    path('find/phone/', views.FindUserByPhone.as_view()),
]
