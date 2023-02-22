from django.db import models

from news.managers import PostManager


class Channel(models.Model):
    name = models.CharField('название', max_length=50)

    class Meta:
        verbose_name = 'канал'
        verbose_name_plural = 'каналы'

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.CharField('текст поста', max_length=4100)
    channel = models.ForeignKey(Channel, related_name='post', verbose_name='название канала', on_delete=models.CASCADE)
    date = models.DateTimeField('дата создания')

    objects = PostManager()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('date',)

    def __str__(self):
        return f'пост {self.pk}'


class Image(models.Model):
    post = models.ForeignKey(Post, verbose_name='пост', related_name='images', on_delete=models.CASCADE)
    photo = models.ImageField('фото', upload_to='media/')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return f'изображение {self.pk}'
