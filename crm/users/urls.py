from django.urls import path

from crm.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)
from crm.users.api.views import UserList,UserDetail
app_name = "users"
urlpatterns = [
    path("list/", UserList.as_view() , name="list"),
    path("detail/<id>/", UserDetail.as_view() , name="UserDetail"),

    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
