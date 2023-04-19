from django.urls import include, path
from blog import views



urlpatterns = [
     path('blog/', views.blog, name='blog'),
     path('contact', views.contact, name='contact'),
     path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
     path('create_blog', views.create_blog, name='create_blog'),
     path('about', views.about, name='about'),
     path('cv/', views.download_cv, name='download_cv'),
     path('resume', views.resume, name='resume'),
     path('services', views.services, name='services'),
]
