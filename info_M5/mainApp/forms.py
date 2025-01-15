from .models import Photo
from django.forms import TextInput,DateTimeInput,ModelForm

class PhotoForm(ModelForm):
	class Meta:
		model = Photo
		fields = ['url', 'date']

		widgets ={
			"url": TextInput(attrs={'class': 'form-control', 'placeholder': 'Вставьте URL ссылку изображения'}),
			"date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату публикации'}),
		}