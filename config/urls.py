from django.contrib import admin
from django.urls import path, include

# Pillow (картинки)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('acoffe.urls')),
]

# Pillow (картинки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'acoffe.views.error_404'
handler403 = 'acoffe.views.error_404'
handler404 = 'acoffe.views.error_404'
# handler500 = 'acoffe.views.error_500'