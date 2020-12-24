from .views import (MoviesViewSet)

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('movies', MoviesViewSet,
                basename='movies')
urlpatterns = router.urls
