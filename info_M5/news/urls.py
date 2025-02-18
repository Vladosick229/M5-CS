from django.urls import path, include
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'news',NewsViewSet,basename='news')
# print(router.urls)

urlpatterns = [
    path('', news_home, name = ('news_home')),
    path('create/', create, name = ('create')),
	path('<int:pk>/',NewsDetailView.as_view(), name = 'news_detail'),
	path('<int:pk>/update/',NewsUpdateView.as_view(), name = 'news_update'),
	path('<int:pk>/delete/',NewsDeleteView.as_view(), name = 'news_delete'),
	path('api/v1/newslist/',NewsAPIList.as_view(), name = 'news_api_list'),
	path('api/v1/newslist/update/<int:pk>/',NewsAPIUpdate.as_view(), name = 'news_update_api'),
	path('api/v1/newslist/delete/<int:pk>/',NewsAPIDestroy.as_view(), name = 'news_delete_api'),
 	# path('api/v1/',include(router.urls)), 	
	# path('api/v1/newslist/',NewsViewSet.as_view({'get':'list'}), name = 'news'),
	# path('api/v1/newslist/<int:pk>/',NewsViewSet.as_view({'put':'update'}), name = 'news_updated'),
	# path('api/v1/newslist/detail/<int:pk>/',NewsAPIDetailView.as_view(), name = 'news_updated'),
]
