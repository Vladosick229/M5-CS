from django.db import models


class Photo(models.Model):
	url = models.URLField(verbose_name="Ссылка на изображение")
	date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.url


	class Meta:
		verbose_name = 'Фотография'
		verbose_name_plural = 'Фотографии'
