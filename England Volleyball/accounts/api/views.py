from django.db.models import Q
from rest_framework import generics, mixins
from accounts.models import Profile
from .permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer


class ProfileAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ProfileSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = Profile.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = filter(Q(user__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}


class ProfileRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProfileSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return Profile.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)
