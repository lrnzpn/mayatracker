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
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    #path('register/', views.UserView.as_view())
]