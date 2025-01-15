from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = ('home')),
	path('about', views.about, name = ('about')),
	path('dynamic', views.dynamic, name = ('dynamic')),
	path('photo', views.photo, name = ('photo')),
	path('create_adding_photo', views.create_adding_photo, name = ('create_adding_photo')),
	path('<int:pk>',views.PhotoDetailView.as_view(), name = 'photo_detail'),
	path('<int:pk>/update',views.PhotoUpdateView.as_view(), name = 'photo_change'),
	path('<int:pk>/delete',views.PhotoDeleteView.as_view(), name = 'photo_delete'),
]
