from django.urls import path
from . import views
from .views import (postlistview,
                    postdetailview,
                    postcreateview,
                    postupdateview,postdeleteview,
                    Userpostlistview,)

urlpatterns = [
    path('', postlistview.as_view(),name='blog-home'),
    path('user/<str:username>', Userpostlistview.as_view(),name='blog-posts'),
    path('post/<int:pk>/', postdetailview.as_view(),name='post-detail'),
    path('post/new/', postcreateview.as_view(),name='post-create'),
    path('post/<int:pk>/update/', postupdateview.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', postdeleteview.as_view(),name='post-delete'),
    path('about/',views.about,name='blog-about')
]