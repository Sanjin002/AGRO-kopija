from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# endpoint je 'crops_api'
router.register('crops_api', views.CropView)
router.register('crops_categories',views.CategoryView)


#
urlpatterns = [
    path('', include(router.urls))
]