from django.urls import path
from rest_framework.routers import DefaultRouter

from news.views import NewsViewSet, NewsByChannelView

app_name = 'news'

router = DefaultRouter()
router.register(r'', NewsViewSet)

urlpatterns = [
    *router.urls,
    path('channel/<int:channel_pk>/', NewsByChannelView.as_view(), name='news_by_channel_list')
]
