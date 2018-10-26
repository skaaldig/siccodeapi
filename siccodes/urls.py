from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'major-group', views.MajorGroupViewSet)
router.register(r'industry-group', views.IndustryGroupViewSet)
router.register(r'industry-sector', views.IndustrySectorViewSet)
router.register(r'sic-code', views.SicCodeViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
