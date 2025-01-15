from .models import Article
from django.forms import ModelForm, TextInput,DateTimeInput,Textarea


class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'anons', 'content', 'date']

		widgets ={
			"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название новости'}),
			"anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите анонс новости'}),
			"date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату публикации'}),
            "content": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст новости'}),
		}