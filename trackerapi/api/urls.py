from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet)
# IF users endpoint is needed, uncomment the next line
# router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
url_prefix = 'api/v1'
urlpatterns = [
    path(f'{url_prefix}/', include(router.urls)),                           # models
    path(f'{url_prefix}/auth/', include('rest_framework.urls')),            # login/logout
    path(f'{url_prefix}/register/', views.RegistrationView.as_view()),       # registration
    path(f'{url_prefix}/login/', TokenObtainPairView.as_view()),
    path(f'{url_prefix}/token/refresh/', TokenRefreshView.as_view()),
    url(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^api/v1/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api/v1/docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]