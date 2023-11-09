from rest_framework import generics
from modules.models import EducationalModule
from modules.paginators import ModulePaginator
from modules.permissions import IsOwner
from modules.serializers import EducationalModuleSerializer
from rest_framework.permissions import IsAuthenticated
from modules.models import EducationalModule


class ModuleCreateAPIView(generics.CreateAPIView):
    """Создание модуля"""
    serializer_class = EducationalModuleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Владельцем становится пользователь"""
        new_module = serializer.save()
        new_module.owner = self.request.user
        new_module.save()


class ModuleListAPIView(generics.ListAPIView):
    """Отображение модулей"""
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()
    pagination_class = ModulePaginator


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение модулей"""
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """Редактирование модуля"""
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()
    permission_classes = [IsOwner]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """Удаление модуля"""
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()
    permission_classes = [IsOwner]


class ModuleUserListAPIView(generics.ListAPIView):
    """Отображение модулей пользователя"""
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()
    pagination_class = ModulePaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Фильтр на пользователя"""
        queryset = EducationalModule.objects.filter(owner=self.request.user)
        return queryset
