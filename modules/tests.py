from rest_framework.test import APITestCase
from modules.models import EducationalModule
from rest_framework.reverse import reverse
from rest_framework import status


class ModulesTestCase(APITestCase):
    """Тесы для модулей по status.HTTP"""
    def setUp(self):
        """Данные для теста"""
        # создаём нового пользователя, отправив запрос к конечной точке djoser
        self.user = self.client.post('/auth/users/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        # получаем веб-токен JSON для вновь созданного пользователя
        response = self.client.post('/auth/jwt/create/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()
        self.module_data = {"title": "testtitle", "description": "testingdescription"}

    def api_authentication(self):
        """Добавляем Authorization в Headers"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    def test_create_module(self):
        """Тест на создание модуля"""
        url = reverse('modules:modules_create')
        response = self.client.post(url, data=self.module_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_module(self):
        """Тест на просмотр модулей"""
        url = reverse('modules:modules_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_module(self):
        """Тест на просмотр модуля"""
        module = EducationalModule.objects.create(title='new title', description='new description')
        url = reverse('modules:modules_get', kwargs={'pk': module.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_module(self):
        """Тест на обновление модуля"""
        # создаём модуль от тестового пользователя так как только он может редактировать её
        url = reverse('modules:modules_create')
        response = self.client.post(url, data=self.module_data)
        updated_module = {'title': 'title for update', 'description': 'test description update'}
        url = reverse('modules:modules_update', kwargs={'pk': response.data['id']})
        response = self.client.patch(url, data=updated_module)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_module(self):
        """Тест на удаление модуля"""
        url = reverse('modules:modules_create')
        response = self.client.post(url, data=self.module_data)
        url = reverse('modules:modules_delete', kwargs={'pk': response.data['id']})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_user_module(self):
        """Тест на просмотр модулей пользователя"""
        url = reverse('modules:user_modules_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
