from django.contrib import admin

from news.models import Post, Image, Channel

admin.site.register(Channel)


class ImagesInline(admin.StackedInline):
    model = Image
    extra = 0
    fields = ('photo',)


@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('text', 'channel', 'date')
    inlines = (ImagesInline,)
