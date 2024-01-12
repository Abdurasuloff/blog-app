from django.urls import path
from .views import index, blog_detail, blog_yarat, blog_tahrirlash, blog_ochirish


urlpatterns = [
    path("", index, name='index'),
    path('blog/<int:blog_id>/', blog_detail, name="blog_detail"),
    path("blog-yarat/", blog_yarat, name='blog_yarat'),
    path("blog-tahrirlash/<int:blog_id>/", blog_tahrirlash, name='blog_tahrirlash'),
    path("blog-ochirish/<int:blog_id>/", blog_ochirish, name='blog_ochirish'),
    
]
