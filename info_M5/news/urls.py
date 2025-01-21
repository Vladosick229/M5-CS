from django.urls import path
from . import views 

urlpatterns = [
    path('', views.news_home, name = ('news_home')),
    path('create/', views.create, name = ('create')),
	path('<int:pk>/',views.NewsDetailView.as_view(), name = 'news_detail'),
	path('<int:pk>/update/',views.NewsUpdateView.as_view(), name = 'news_update'),
	path('<int:pk>/delete/',views.NewsDeleteView.as_view(), name = 'news_delete'),
	path('api/v1/newslist/',views.NewsAPIList.as_view(), name = 'news'),
	path('api/v1/newslist/<int:pk>/',views.NewsAPIUpdate.as_view(), name = 'news_updated'),
	path('api/v1/newslist/detail/<int:pk>/',views.NewsAPIDetailView.as_view(), name = 'news_updated'),
]
