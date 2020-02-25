from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
)
from . import views

urlpatterns = [
    path('', views.index, name='survey-home'),
    path('survey-new/', views.post_new, name='post_new'),
    path('<int:post_id>', views.post, name='survey2'),
    path('new/', PostCreateView.as_view(), name='survey-new'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('new2/', views.post_form, name='post_form'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path("pdf/<str:pk>/", views.post_receipt, name="post_receipt",
         ),
]
