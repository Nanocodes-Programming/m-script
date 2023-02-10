from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nanoadmin/', admin.site.urls),
    path('',include('base.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls')),
    path('admin/', include('custom_admin.urls')),
    #path('face/', include('face_id.urls')),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'user.views.my_custom_page_not_found_view'
handler400 = 'user.views.my_custom_bad_request_view'
handler403 = 'user.views.my_custom_permission_denied_view'
handler500 = 'user.views.my_custom_error_view'


