from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Article
from .permissions import CustomerAccessPermission
from .serializers import ArticleSerializer, CreateArticleSerializer


@api_view(['GET'])
def view_all_articles(request):
    articles = Article.objects.all().order_by('-time_update')
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def view_article(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except:
        return Response({'error': 'Object does not exist'})
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_article(request, pk):
    data = request.data

    try:
        article = Article.objects.get(id=pk)
    except:
        return Response({'error': 'Object does not exist'})

    serializer = ArticleSerializer(instance=article, data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([CustomerAccessPermission])
def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return Response('Article was deleted')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    data = request.data
    article = Article.objects.create(
        title=data['title'],
        content=data['content'],
        category=data['category'],
    )
    serializer = CreateArticleSerializer(article, many=False)
    return Response(serializer.data)
