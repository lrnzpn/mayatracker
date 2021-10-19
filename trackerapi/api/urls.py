from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers
from . import views

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
    path(f'{url_prefix}/register/', views.RegistrationView.as_view())       # registration
]