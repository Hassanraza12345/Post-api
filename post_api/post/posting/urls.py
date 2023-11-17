from .views import Postview
from django.urls import path ,include
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Posting',Postview)


urlpatterns = [
    path('', include(router.urls))
]