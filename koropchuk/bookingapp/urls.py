from django.urls import path, include

from .views import *
from rest_framework import routers


# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]
#
#
# # router = routers.SimpleRouter()
# # router = routers.DefaultRouter()
# router = MyCustomRouter()
# router.register(r'bookingpier', BookingPierViewSet, basename='bookingpier')
# print(router.urls)


urlpatterns = [
   path('api/v1/bookingpier/', BookingPierAPIList.as_view(), name='bookingapier_rest'),
   path('api/v1/bookingpier/<int:pk>/', BookingPierAPIUpdate.as_view()),
   path('api/v1/bookingpierdelete/<int:pk>/', BookingPierAPIDestroy.as_view()),
    # path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/bookingpier/
    # path('api/v1/bookingpierlist/', BookingPierViewSet.as_view({'get': 'list'})),
    # path('api/v1/bookingpierlist/<int:pk>/', BookingPierViewSet.as_view({'put': 'update'})),
#    path('api/v1/bookingpierlist/', BookingPierAPIList.as_view()),
#    path('api/v1/bookingpierlist/<int:pk>/', BookingPierAPIUpdate.as_view()),
#    path('api/v1/bookingpierdetail/<int:pk>/', BookingPierAPIDetailView.as_view()),
#    path('api/v1/bookingpierlist/<int:pk>/', BookingPierAPIList.as_view()),
#    path('api/v1/bookingpierlist/', BookingPierAPIView.as_view()),
#    path('api/v1/bookingpierlist/<int:pk>/', BookingPierAPIView.as_view()),
]
