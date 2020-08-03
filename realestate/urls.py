from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.url')),
    path('listings/', include('listings.url')),
    path('admin/', admin.site.urls),
]
