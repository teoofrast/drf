from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import routers
from magazine.views import *

router = routers.SimpleRouter()
router.register(r'watch', WatchAPIViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'basket', AddToCart)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth', include('rest_framework.urls')),
]
