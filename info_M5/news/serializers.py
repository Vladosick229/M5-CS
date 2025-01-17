from rest_framework import serializers
from .models import Article
     
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    anons = serializers.CharField()
    content = serializers.CharField(read_only=True)
    date = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.anons = validated_data.get('anons', instance.anons)
        instance.content = validated_data.get('content', instance.content)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

        