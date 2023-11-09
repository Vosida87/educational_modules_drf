from modules.apps import ModulesConfig
from django.urls import path
from modules.views import *

app_name = ModulesConfig.name

urlpatterns = [
    path('modules/create/', ModuleCreateAPIView.as_view(), name='modules_create'),
    path('modules/', ModuleListAPIView.as_view(), name='modules_list'),
    path('modules/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='modules_get'),
    path('modules/update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='modules_update'),
    path('modules/delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='modules_delete'),
    path('user_modules/', ModuleUserListAPIView.as_view(), name='user_modules_list')
]
