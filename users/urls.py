from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserListCreateView, UserRetrieveUpdateDestroyView

app_name = UsersConfig.name

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="users"),
    path("user_create/", UserListCreateView.as_view(), name="user-create"),
    path(
        "update_delete_retrive/<int:pk>/",
        UserRetrieveUpdateDestroyView.as_view(),
        name="user-retrieve-update-destroy",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
