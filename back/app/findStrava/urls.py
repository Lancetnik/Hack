from django.urls import path

from . import views


urlpatterns = (
    path('polyline/', views.GetPolyline.as_view()),
)
