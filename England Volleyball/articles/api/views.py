from django.db.models import Q
from rest_framework import generics, mixins
from articles.models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from rest_framework import permissions


class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly,)
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(user__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly,)
    # queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)
