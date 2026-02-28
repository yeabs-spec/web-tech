from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from hospitalpages.views import home,details


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='homelink'),
    path('detail/',details,name='detailslink'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
