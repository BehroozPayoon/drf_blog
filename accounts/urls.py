from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet

router = SimpleRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = router.urls
