from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("vik", views.HelloWorldSETS, basename='viktor')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')



urlpatterns = [
    path('hello/', views.HellowWORLD.as_view()),
    path('', include(router.urls)),
]

