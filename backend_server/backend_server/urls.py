from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^read_log/', include('log_streamer.urls')),
    url(r'^admin/', admin.site.urls),
]
