from django.urls import path
from .views import  HomePageView, AboutPageView, ArticlePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),

    path('article/', ArticlePageView.as_view(), name = 'article')



]