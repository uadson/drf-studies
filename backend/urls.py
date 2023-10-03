from django.contrib import admin
from django.urls import path, include

from intermediary_v2.urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs DRF
    path('api/auth/', include('rest_framework.urls')),

    # URLs Basic (endpoints)
    path('api/v1/basic/', include('basic.urls', namespace='basic')),

    # URLs Intermediary (endpoints)
    path('api/v1/interm/', include('intermediary.urls', namespace='intermediary')),

    # URLs Intermediary v2 (automatic endpoints)
    path('api/v2/interm/', include(router.urls)),
]
