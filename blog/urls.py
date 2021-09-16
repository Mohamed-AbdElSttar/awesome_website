from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path("", blog_views.listing, name="listing"),
    path("view_blog/<int:blog_id>/", blog_views.view_blog, name="view_blog"),
    path("see_request/", blog_views.see_request),
    path("user_info/", blog_views.user_info),
    path("private_place/", blog_views.private_place),
    path("staff_place/", blog_views.staff_place),
    path("add_messages/", blog_views.add_messages),
]