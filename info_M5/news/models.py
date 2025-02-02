from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
	title = models.CharField('Название',max_length=50)
	anons = models.CharField('Анонс',max_length=250)
	content = models.TextField('Статья')
	date = models.DateTimeField('Дата публикации')
	user = models.ForeignKey(User,verbose_name ='Пользователь',on_delete=models.CASCADE)

	def __str__(self):
		return f'Новость: {self.title}'

	def  get_absolute_url(self):
		return f'/news/{self.id}'
	

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

