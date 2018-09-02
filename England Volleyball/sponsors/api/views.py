from django.db.models import Q
from rest_framework import generics, mixins
from sponsors.models import Sponsor
from .permissions import IsOwnerOrReadOnly
from .serializers import SponsorSerializer


class SponsorAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SponsorSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = Sponsor.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = filter(Q(name__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}


class SponsorRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SponsorSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return Sponsor.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)
