from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView,UpdateView,DeleteView


def news_home(request):
	news = Article.objects.order_by('-date')
	return render(request, 'news/news_home.html',{'title':'News about M5 CS','news': news})


class NewsDetailView(DetailView):
	model= Article
	template_name = 'news/news_detail.html'
	context_object_name = 'article'

class NewsUpdateView(UpdateView):
	model= Article
	template_name = 'news/news_update.html'
	form_class = ArticleForm

class NewsDeleteView(DeleteView):
	model= Article
	success_url = '/news/'
	template_name = 'news/news_delete.html'


def create(request):
	error = ''
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = 'Форма заполнена неверно! Попробуйте еще раз.'

	form = ArticleForm()

	data = {
		'form': form,
		'error': error,
		'title': 'Creating an article',
	}

	return render(request, 'news/create.html',data)

