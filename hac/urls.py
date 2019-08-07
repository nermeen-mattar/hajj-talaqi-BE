"""hac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from containers.views import ContainersViewSet
from members.views import MembersViewSet
from reservation_scans.views import ReservationScansViewSet
from reservations.views import ReservationsViewSet
from scans.views import ScansViewSet
from offices.views import OfficesViewSet
from supervisor.views import SupervisorsViewSet
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title=' API')
uuid_pattern = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
office = "(?P<office_id>%s)" % uuid_pattern

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UsersViewSet)
router.register(r'containers', ContainersViewSet)
router.register(r"%s/members" % office, MembersViewSet)
router.register(r'%s/reservation_scans' % office, ReservationScansViewSet)
router.register(r'%s/reservations' % office, ReservationsViewSet)
router.register(r'%s/scans' % office, ScansViewSet)
router.register(r'%s/supervisors' % office, SupervisorsViewSet)
router.register(r'offices', OfficesViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    # url(r'^pa', schema_view)


]
