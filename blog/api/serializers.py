from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Article
        exclude = ['slug']


class CreateArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        exclude = ['slug']
