from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic.base import TemplateView

from vng_api_common.views import ViewConfigView

handler500 = "nrc.utils.views.server_error"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("adfs/", include("django_auth_adfs.urls")),
    path("oidc/", include("mozilla_django_oidc.urls")),
    path("api/", include("nrc.api.urls")),
    # Simply show the master template.
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("ref/", include("vng_api_common.urls")),
    path("view-config/", ViewConfigView.as_view(), name="view-config"),
]

# NOTE: The staticfiles_urlpatterns also discovers static files (ie. no need to run collectstatic). Both the static
# folder and the media folder are only served via Django if DEBUG = True.
urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
