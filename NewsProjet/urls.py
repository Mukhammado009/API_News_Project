from django.contrib import admin
from django.urls import path, include
from news.views import CustomUserAPIView, NewsAPIView, NewsDetailAPIView, CommentAPIView, CommentDetailAPIView,  LatestNewsAPIView,  MostViewedNewsAPIView, LastFiveNewsAPIView,SaveAPIView,SaveDetailAPIView,NewsSearchAPIView           


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/', CustomUserAPIView.as_view()),
    
    path('news/', NewsAPIView.as_view()),
    path('news/<int:pk>/', NewsDetailAPIView.as_view()),
    
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view()),
    
    
    path('news/latest/', LatestNewsAPIView.as_view()),
    path('news/most-viewed/', MostViewedNewsAPIView.as_view()),
    path('news/last-5/', LastFiveNewsAPIView.as_view()),
    
    path('news/save/', SaveAPIView.as_view()),
    path('news/save/<int:pk>/', SaveDetailAPIView.as_view()),
    
    path('', include('news.drf_yasg')),
    
     path('api/search/', NewsSearchAPIView.as_view()),
    
    

]


    

