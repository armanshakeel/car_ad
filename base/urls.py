from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('users/create/',views.createUser),
    path('users/<str:pk>/update/',views.updateUser),
    path('users/ads/create/',views.createads),
    path('users/ads/<str:pk>/update/',views.updateads),
    path('users/ads/<str:pk>/delete/',views.deleteads),
    path('users/ads/',views.getads),
]