from django.shortcuts import render
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView
from rest_framework import mixins 
from .models import News, Comment, CustomUser, Save 
from .serializers import NewsSerializer, CommentSerializer, CustomUserSerializer, SaveSerializer
from rest_framework import generics
from rest_framework import status
from django.db.models import Q


class CustomUserAPIView(ListAPIView,CreateAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
        
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class NewsAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'    
    
    def perform_create(self, serializer):
        news_id = self.kwargs.get('news_id')  
        serializer.save(auth=self.request.user, news_id=news_id)
 
  

class NewsSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        
        if query:
            search_filter = Q(tittle__icontains=query) | Q(content__icontains=query)
            results = News.objects.filter(search_filter)
            
            serializer = NewsSerializer(results, many=True)
            return Response(serializer.data)
        return Response({"detail": "No query parameter provided."}, status=status.HTTP_400_BAD_REQUEST)
 
 
class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'    
    
    def perform_create(self, serializer):
        news_id = self.kwargs.get('news_id')  
        serializer.save(author=self.request.user, news_id=news_id)
 


class MostViewedNewsAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-views')
    serializer_class = NewsSerializer
 

class LatestNewsAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer


class LastFiveNewsAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by('-created_at')[:5]


class SaveAPIView(generics.ListCreateAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    
class SaveDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    lookup_field = 'pk'    
 
 