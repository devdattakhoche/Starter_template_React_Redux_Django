from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('api/', include('backend.api.urls')),
    path('admin/', admin.site.urls),
]