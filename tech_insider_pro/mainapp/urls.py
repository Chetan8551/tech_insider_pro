
from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [

    # HOME
    path('', views.home, name='home'),

    # BLOG
    path('blog/', views.blog, name='blog'),

    # SEO FRIENDLY BLOG DETAIL
    path(
        'blog/<int:pk>/<slug:slug>/',
        views.post_detail,
        name='post_detail'
    ),

    # REVIEWS
    path (
        'reviews/<slug:slug>/',
        views.review_detail,
        name='review_detail'
    ),

    # STATIC PAGES
    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('disclaimer/', views.disclaimer, name='disclaimer'),

    # LEGAL PAGES
    path(
        'privacy-policy/',
        views.privacy_policy,
        name='privacy_policy'
    ),

    path(
        'affiliate-disclosure/',
        views.affiliate_disclosure,
        name='affiliate_disclosure'
    ),

    path(
        'terms-and-conditions/',
        views.terms_conditions,
        name='terms_conditions'
    ),

    # SUBSCRIBE
    path(
        'subscribe/',
        views.subscribe,
        name='subscribe'
    ),

    # SEO
    path(
        'robots.txt',
        views.robots_txt,
        name='robots_txt'
    ),

    path(
        'sitemap.xml',
        views.sitemap_xml,
        name='sitemap_xml'
    ),
]

