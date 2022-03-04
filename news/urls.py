from django.urls import path
from django.views.decorators.cache import cache_page
from .views import News, NewsDetailView, Search, PostCreateView, NewsUpdateView, NewsDeleteView, upgrade_me, subscribe_me



urlpatterns = [
    path('', cache_page(60)(News.as_view())),
    path('<int:pk>', NewsDetailView.as_view(), name='post'),
    path('search/', Search.as_view()),
    path('add/', PostCreateView.as_view()),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='post_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('subscribed/<int:news_category_id>', subscribe_me, name='subscribed'),
]
