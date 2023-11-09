from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.contrib.auth.models import User

NULLABLE = {'blank': True, 'null': True}


class EducationalModule(models.Model):
    """Модель образовательных модулей"""
    # Порядковый номер - идентификатор id
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель модуля', **NULLABLE)
    title = models.CharField(max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator(50)])
    description = models.TextField(validators=[RegexValidator(r'^[A-Za-z0-9 ]+$', message='Только цифро буквенные '
                                                                                          'значения')])

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return f'Владелец {self.owner}, модуль: {self.title}'
