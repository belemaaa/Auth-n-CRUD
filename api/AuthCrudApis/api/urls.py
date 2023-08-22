from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('post/create/', views.PostView.as_view()),
    path('post/', views.PostView.as_view()),
    path('post/user/', views.GetUserPosts.as_view()),
    path('post/<int:pk>/', views.PostView.as_view()),
    path('post/<int:pk>/update/', views.PostView.as_view()),
    path('post/<int:pk>/delete/', views.PostView.as_view()),
]