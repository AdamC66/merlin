from django.urls import path, include

from django.conf.urls.static import static
from django.urls import re_path, path
from apps.merlin_user.rest.api import MerlinUserViewSet

urlpatterns = [
    re_path(r'^user/(?P<user_code>[\w-]+)/', MerlinUserViewSet.as_view()),
    path('user/', MerlinUserViewSet.as_view()),
]
