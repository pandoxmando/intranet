from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("asset/", include("asset.urls")),
    path("handover/", include("handover.urls")),
    path("staff/", include("staff.urls")),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
