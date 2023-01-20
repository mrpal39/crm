from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

from crm.users.api.views import UserViewSet,UserList

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
# router.register("users-list", UserList)

# The API URLs are now determined automatically by the router.
app_name = "api"
urlpatterns = [
    path('', include(router.urls)),
    path('user-list', UserList.as_view()),
]

