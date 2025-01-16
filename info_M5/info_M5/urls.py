from django.contrib import admin
from django.urls import path,include
from news.views import NewsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('mainApp.urls')),
	path('news/', include('news.urls')),
 	path('api/v1/news',NewsAPIView)
]
