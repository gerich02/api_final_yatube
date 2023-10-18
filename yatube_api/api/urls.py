from django.urls import include, path

from rest_framework import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(
    'posts',
    PostViewSet,
    basename='posts'
)
router_v1.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
router_v1.register(
    'follow',
    FollowViewSet,
    basename='follows'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
