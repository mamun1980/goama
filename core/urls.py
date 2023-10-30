from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="popular-queries")),
    path('api/', include('apps.goam_number.urls')),
    # path('admin/', admin.site.urls),
]
