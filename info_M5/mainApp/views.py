from django.shortcuts import render,redirect
from .models import Photo
from .forms import PhotoForm
from django.views.generic import DetailView, UpdateView,DeleteView

def home(request):
	data={'title':'BMW M5 CS',
	   'values':['BMW','M5', 'CS']}
	return render(request, 'mainApp/homePage.html',data)

def about(request):
	return render(request, 'mainApp/aboutPage.html',{'title':'About M5 CS'})

def dynamic(request):
	return render(request, 'mainApp/dynamicPage.html',{'title':'Dynamic M5 CS'})

def photo(request):
	photo = Photo.objects.order_by('-date')
	return render(request, 'mainApp/photoPage.html',{'title':'Photo M5 CS','photo':photo})


class PhotoDetailView(DetailView):
	model= Photo
	template_name = 'mainApp/photo_detail.html'
	context_object_name = 'photo'

class PhotoUpdateView(UpdateView):
	model= Photo
	template_name = 'mainApp/photo_change.html'
	form_class = PhotoForm

class PhotoDeleteView(DeleteView):
	model= Photo
	success_url = '/photo/'
	template_name = 'mainApp/photo_delete.html'

def create_adding_photo(request):
	error = ''
	if request.method == 'POST':
		form = PhotoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Photo_home')
		else:
			error = 'Форма заполнена неверно! Попробуйте еще раз.'

	form = PhotoForm()

	data = {
		'form': form,
		'error': error,
		'title': 'Creating a photo',
	}

	return render(request, 'mainApp/create_adding_photo.html',data)