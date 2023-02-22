from rest_framework.viewsets import ModelViewSet

from news.models import Post
from news.serializers import PostSerializer
from news.permisions import NoAccess


class NewsView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):

        if self.action in ('list', 'retrieve'):
            permission_classes = []
        else:
            permission_classes = [NoAccess]
        return [permission() for permission in permission_classes]
