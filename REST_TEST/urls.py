from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("vik", views.HelloWorldSETS, basename='viktor')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('expenses', views.ExpensesViewSet)
router.register('zarplata', views.IncomeViewSet)


urlpatterns = [
    path('hello/', views.HellowWORLD.as_view()),
    path('', include(router.urls)),
]

