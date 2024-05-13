from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("create/",views.PostCreateView.as_view(),name="post_create"),
    path("<slug:slug>/",views.post_detail,name="post_detail"),
    path("<slug:slug>/update/",views.PostUpdateView.as_view(),name="post_update"),
    path("<slug:slug>/delete/",views.PostDeleteView.as_view(),name="post_delete"),
    path('comment/<int:pk>/delete/', views.DeleteCommentView.as_view(), name='delete_comment'),
]
