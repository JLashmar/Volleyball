from django.shortcuts import render
from articles.models import Post
from django.views.generic import ListView

# Create your views here.


class IndexView(ListView):
    template_name = "articles/index.html"
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        context = {'all_posts': Post.objects.all()}
        #context['headline'] = Post.objects.exclude(headline_image='')
        #context['top_headline'] = Post.objects.filter(headline_image__exact='')
        #context['videos'] = VideoNews.objects.all()
        return context

    def get_queryset(self):
        return Post.objects.all()
