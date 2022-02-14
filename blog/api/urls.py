from django.urls import path
from . import views

urlpatterns = [
    path('v1/articles/', views.view_all_articles, name='articles'),
    path('v1/article-create/', views.create_article, name='article-create'),
    path('v1/article/<int:pk>', views.view_article, name='article'),
    path('v1/article-update/<int:pk>', views.update_article, name='update-article'),
    path('v1/article-delete/<int:pk>', views.delete_article, name='delete-article'),
]
