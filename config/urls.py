from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .api import (
    AutherListAPI,
    AutherDetailAPI,
    BookListAPI,
    BookDetailAPI,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list/', BookListAPI.as_view()),
    path('api/list/<int:pk>/', BookDetailAPI.as_view()),
    path('api/list/auther/', AutherListAPI.as_view()),
    path('api/list/auther/<int:pk>/', AutherDetailAPI.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
