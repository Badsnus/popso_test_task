from rest_framework.routers import DefaultRouter

from news.views import NewsView

app_name = 'news'

router = DefaultRouter()
router.register(r'', NewsView, basename='news')

urlpatterns = [
    *router.urls,

]
