from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('details/<int:id>/', views.details, name='details'),

]
