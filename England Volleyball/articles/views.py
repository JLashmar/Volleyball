from django.shortcuts import get_object_or_404
from articles.models import Post
from clubs.models import Club
from django.views.generic import ListView, DetailView
import requests
import coreapi
import json
from . import services
from rest_framework.views import APIView


class IndexView(ListView):
    template_name = "articles/index.html"
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        parsedData = []
        context = {'all_posts': Post.objects.all()}
        context['subArticle'] = Post.objects.filter(image__exact='')
        context['mainArticle'] = Post.objects.exclude(image='')
        #context['videos'] = VideoNews.objects.all()
        r = requests.get('http://127.0.0.1:8000/api/posts/')
        data = r.json()
        context['parsedData'] = parsedData
        for game in data:
            cardData = {}
            cardData['url'] = game['url']
            cardData['club'] = game['club']
            cardData['title'] = game['title']
            cardData['post_slug'] = game['post_slug']
            cardData['short_description'] = game['short_description']
            cardData['body'] = game['body']
            parsedData.append(cardData)
        return context

    def get_queryset(self):
        return Post.objects.all()


class ClubView(ListView):
    template_name = "articles/club_index.html"
    context_object_name = "all_posts"

    def get_context_data(self, **kwargs):
        self.club = get_object_or_404(Club, club_slug=self.kwargs['club_slug'])
        context = {'all_posts': Post.objects.filter(club=self.club)}
        return context

    def get_queryset(self):
        self.club = get_object_or_404(Club, club_slug=self.kwargs['club_slug'])
        return Post.objects.filter(club=self.club)


class DetailView(DetailView):
    #queryset = Post.objects.all()
    slug_url_kwarg = 'post_slug'
    template_name = 'articles/details.html'
    slug_field = 'post_slug'

    def get_slug_field(self):
        return self.slug_field

    def post_projects(self):
        self.post = get_object_or_404(Post, slug=self.kwargs['post_slug'])
        return Post.objects.filter(post=self.post)

    def get_queryset(self):
        self.club = get_object_or_404(Club, club_slug=self.kwargs['club_slug'])
        return Post.objects.filter(club=self.club)
