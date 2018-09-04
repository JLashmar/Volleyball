from django.db.models import Q
from rest_framework import generics, mixins
from leagues.models import League, LeagueTable, LeagueTableData
from .permissions import IsOwnerOrReadOnly
from .serializers import LeagueSerializer, LeagueTableSerializer, LeagueTableDataSerializer

##########
# League #
##########


class LeagueAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = LeagueSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = League.objects.all()
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


class LeagueRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = LeagueSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return League.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)

###############
#League Table #
###############


class LeagueTableAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = LeagueTableSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = LeagueTable.objects.all()
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


class LeagueTableRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = LeagueTableSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return LeagueTable.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)

####################
#League Table Data #
####################


class LeagueTableDataAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = LeagueTableDataSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = LeagueTableData.objects.all()
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


class LeagueTableDataRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = LeagueTableDataSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return LeagueTableData.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return{"request": self.request}

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return Post.objects.get(pk=pk)
