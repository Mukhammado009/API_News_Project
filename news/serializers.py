from rest_framework import serializers
from .models import CustomUser, News, Comment, Category, Save


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
    
        

class NewsSerializer(serializers.ModelSerializer):
     class Meta:
        model = News
        fields =  ['id','tittle', 'content', 'views', 'category', 'auth', 'created_at'] 
        read_only_fields = ['auth', 'created_at']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ['id','text', 'created_at', 'news', 'author']
        read_only_fields = ['author', 'created_at']  
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = Category  
       fields = '__all__'       
        

class SaveSerializer(serializers.ModelSerializer):
   class Meta:
    model = Save        
    fields = '__all__'
