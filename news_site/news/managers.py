from django.db.models import Manager


class PostManager(Manager):
    def get_posts_by_channel(self, channel_pk: int):
        return self.get_queryset().filter(channel=channel_pk)
