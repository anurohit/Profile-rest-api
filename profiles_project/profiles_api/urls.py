from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view(),name='helloapi'),
    path('',include(router.urls))
]
