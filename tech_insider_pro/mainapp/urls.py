from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('reviews/<slug:slug>/', views.review_detail, name="review_detail"),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]
