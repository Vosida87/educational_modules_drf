from django.urls import path
from accounts.views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    # Забирает всех пользователей + создаёт профиль
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # Для работы с профилем авторизированного пользователя
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
]
