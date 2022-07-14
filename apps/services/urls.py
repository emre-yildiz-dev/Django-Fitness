from django.urls import path
from .views import ClassesPageView, PricingPageView, ClassDetailPageView, SearchResultsListView, comment_post

urlpatterns = [
    path('', ClassesPageView.as_view(), name='classes'),
    path('<int:pk>/', ClassDetailPageView.as_view(), name='class-detail'),
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('comment-post', comment_post, name='comment-post'),
    path('search/', SearchResultsListView.as_view(), name='search-results'),
]
