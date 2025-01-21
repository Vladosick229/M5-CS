from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView,UpdateView,DeleteView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer



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

class NewsAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class NewsAPIUpdate(generics.UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	

class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	
class NewsAPIView(APIView):
    
    # def put(self, request,*args,**kwargs):
    #     pk = kwargs.get('pk',None)
    #     if not pk:
    #         return Response({'error': 'Incorrectly specified article'})
        
    #     try:
    #         instance = Article.objects.get(pk=pk)
    #     except:
    #         return Response({'error': 'Article not found'})
        
    #     serializer = ArticleSerializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'updated': serializer.data})
    
    
    def delete(self, request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error': 'Article not found'})
        
        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({'error': 'Article not found'})
        
        instance.delete()
        return Response({'message':'Deletion was successful'})


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

