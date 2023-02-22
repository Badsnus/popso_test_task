from rest_framework import serializers

from news.models import Post, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('photo',)


class PostSerializer(serializers.ModelSerializer):
    chanel_name = serializers.CharField(source='channel.name')
    images = ImageSerializer(many=True)

    class Meta:
        model = Post
        fields = ('text', 'date', 'chanel_name', 'images')
