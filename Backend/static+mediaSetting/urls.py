from django.conf import settings
from django.conf.urls.static import static
#debugging 할때만 쓰자
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
