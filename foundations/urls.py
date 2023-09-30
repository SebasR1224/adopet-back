from django.urls import path, include
from rest_framework import routers
from foundations import views

#api versioning
router = routers.DefaultRouter()
router.register(r'foundations', views.FoundationView, 'foundations')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
