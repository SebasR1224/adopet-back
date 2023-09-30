from django.urls import path, include
from rest_framework import routers
from animals import views

#api versions
router = routers.DefaultRouter()
router.register(r'animals', views.AnimalsView, 'animals')

urlpatterns = [
    path("api/v1/", include(router.urls))
]