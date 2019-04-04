from django.urls import path
from . import views

app_name = 'article'
#/articles/
urlpatterns = [
    path('', views.articles, name = 'articles'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('addarticle/', views.addarticle, name = 'addarticle'),
    path('comment/<int:id>', views.addComment, name = 'addComment'),
    path('article/<int:id>', views.detail, name = 'articleDetail'),
    path('update/<int:id>', views.update, name = 'updateArticle'),
    path('delete/<int:id>', views.delete, name = 'deleteArticle'),
]