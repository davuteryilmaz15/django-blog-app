from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib  import messages
from .forms import ArticleForm
from .models import Article, Comment

# Create your views here.

def index(request):
    #return HttpResponse("Hello world")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def articles(request):
    keyword = request.GET.get('keyword')
    if keyword is not None:
        articles = Article.objects.filter(title__contains=keyword)
    else:
        articles = Article.objects.all()
    return render(request, 'articles.html', {"articles":articles})

@login_required(login_url = 'user:userLogin')
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url = 'user:userLogin')
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, 'Makale Başarıyla Eklendi.')
        return redirect('article:dashboard')

    context = {
        "form" : form
    }
    return render(request, 'addarticle.html', context)

def detail(request,id):
    #article = get_object_or_404(Article, id = id)
    article = Article.objects.filter(id = id).first()
    if article is None:
        messages.error(request, 'Böyle bir makale bulunmuyor.')
        return redirect('index')
    
    comments = article.comments.all()

    context = {
        "article" : article,
        "comments" : comments,
    }
    return render(request, 'detail.html', context)

def addComment(request,id):
    article = get_object_or_404(Article, id = id)

    if request.method == "POST":
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')

        if comment_author and comment_content:
            newComment = Comment(comment_author = comment_author, comment_content = comment_content, article = article)
            newComment.save()
            messages.success(request, 'Yorum Başarıyla eklendi.')

    return redirect(reverse('article:articleDetail', kwargs={"id":id}))

@login_required(login_url = 'user:userLogin')
def update(request,id):
    article = get_object_or_404(Article, id = id, author = request.user)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Makale Başarııyla Güncelelndi.')
        return redirect('article:dashboard')
    return render(request, 'updatearticle.html', {"form":form})

@login_required(login_url = 'user:userLogin')
def delete(request,id):
    article = Article.objects.get(id = id, author = request.user)
    if article is not None:
        article.delete()
        messages.success(request, 'Makale Başarıyla Silindi.')
    else:
        messages.error(request, 'Böyle bir makaleniz bulunmuyor.')

    return redirect('article:dashboard')
