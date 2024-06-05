from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, get_watch_details

urlpatterns = [
    path('', index, name='index'),
    path('watch/<int:id>/', get_watch_details, name='get_watch_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
