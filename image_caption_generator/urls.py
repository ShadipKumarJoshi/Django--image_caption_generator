from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from captions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_image, name='upload_image'),
    path('captions/', include('captions.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)