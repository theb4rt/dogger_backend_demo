from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api_login.views import CreateUserAPI, LogoutView
from api_login.auth.viewset import LoginViewSet, RefreshViewSet

routes = SimpleRouter()

routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
#routes.register(r'auth/logout', LogoutView.as_view(), basename='auth-logout')
urlpatterns = [
    path('register/user/', CreateUserAPI.create_user),
    path('auth/logout/', LogoutView.as_view(),name='auth-logout'),
    *routes.urls
]
