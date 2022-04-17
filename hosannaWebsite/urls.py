from django.urls import path
from . import views
from .views import Course, Event, EventDetail, News, NewsDetail, course_detail

urlpatterns = [
    path('', views.index, name='home-url'),
    path('courses/', Course.as_view(), name='course-url'),
    path('courses/<slug:slug>', course_detail.as_view(), name='course-detail'),
    path('courses/?category=<int:category>', Course.as_view(), name='category-url'),
    path('subscription/', views.subscription, name='subscription-url'),
    path('about/', views.about, name='about-url'),
    path('event/', Event.as_view(), name='event-url'),
    path('event/<slug:slug>', EventDetail.as_view(), name='event-detail'),
    path('news/', News.as_view(), name='news-url'),
    path('news/<slug:slug>', NewsDetail.as_view(), name='news-detail'),
    path('news/?tag=<int:tag>', News.as_view(), name='tag-url'),
    path('contact/', views.contact, name='contact-url'),
    path('register/<str:name>', views.register, name='registration-url'),
    path('form/', views.download_file, name='form-url')
]