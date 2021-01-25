from django.db import models


class Artiсles(models.Model):
    title = models.CharField('Загаловаок задачи', max_length=100)
    description = models.TextField('Описание задачи')
    date = models.DateField('Дедлайн')
    performed = models.BooleanField('Выполнено', default = False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/work/{self.id}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'