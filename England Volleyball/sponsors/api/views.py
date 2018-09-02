from django.db.models import Q
from rest_framework import generics, mixins
from sponsors.models import Sponsor, ClubSponsor
from .permissions import IsOwnerOrReadOnly
from .serializers import SponsorSerializer, ClubSponsorSerializer, TeamSponsorSerializer, PlayerSponsorSerializer

###############
#Sponsor Lists#
###############


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

##################
#Club Sponsorship#
##################


class ClubSponsorAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ClubSponsorSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = ClubSponsor.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = filter(Q(club__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}


class ClubSponsorRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ClubSponsorSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return ClubSponsor.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)

###############
#team sponsors#
###############


class TeamSponsorAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = TeamSponsorSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = TeamSponsor.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = filter(Q(team__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}


class TeamSponsorRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TeamSponsorSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return TeamSponsor.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)

#################
#Player sponsors#
#################


class PlayerSponsorAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PlayerSponsorSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = PlayerSponsor.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = filter(Q(player__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}


class PlayerSponsorRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PlayerSponsorSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return PlayerSponsor.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)
