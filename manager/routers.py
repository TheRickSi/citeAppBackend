from users.views import MemberViewSet
from cites.views import CiteViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'cite', CiteViewset)

urlpatterns = router.urls