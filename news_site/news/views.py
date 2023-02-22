from rest_framework import viewsets, generics

from news.models import Post
from news.serializers import PostSerializer
from news.permisions import NoAccess


class NewsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):

        if self.action in ('list', 'retrieve'):
            permission_classes = []
        else:
            permission_classes = [NoAccess]
        return [permission() for permission in permission_classes]


class NewsByChannelView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.get_posts_by_channel(self.kwargs['channel_pk'])
