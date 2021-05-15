from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.contrib.auth import views as auth_views

app_name = 'accounts'

router = SimpleRouter()

# router.register('', UserViewSet, basename='user')


urlpatterns = [
    path('', include((router.urls, 'accounts')))
]
