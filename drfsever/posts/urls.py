
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter() #DefaultRouter를 설정
router.register('Post', views.PostViewSet) #itemviewset 과 Post이라는 router 등록

urlpatterns = [
    path('', include(router.urls)),
]
