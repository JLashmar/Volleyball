from django.db.models import Q
from rest_framework import generics, mixins
from clubs.models import Club, Team
from .permissions import IsOwnerOrReadOnly
from .serializers import ClubSerializer, TeamSerializer

##################
#Club Sponsorship#
##################


class ClubAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ClubSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = Club.objects.all()
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


class ClubRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ClubSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return Club.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)

###############
#team sponsors#
###############


class TeamAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = TeamSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = Team.objects.all()
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


class TeamRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TeamSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return Team.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)
