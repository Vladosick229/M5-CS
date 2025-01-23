from django.urls import path
from views import * 

urlpatterns = [
    path('', home, name = ('home')),
	path('about/', about, name = ('about')),
	path('dynamic/', dynamic, name = ('dynamic')),
	path('photo/', photo, name = ('photo')),
	path('create_adding_photo/', create_adding_photo, name = ('create_adding_photo')),
	path('<int:pk>/',PhotoDetailView.as_view(), name = 'photo_detail'),
	path('<int:pk>/update/',PhotoUpdateView.as_view(), name = 'photo_change'),
	path('<int:pk>/delete/',PhotoDeleteView.as_view(), name = 'photo_delete'),
]
