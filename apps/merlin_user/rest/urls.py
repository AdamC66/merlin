from django.urls import path, include

from django.conf.urls.static import static
from django.urls import re_path, path
from apps.merlin_user.rest.api import MerlinUserViewSet

urlpatterns = [
    path('user/', MerlinUserViewSet.as_view()),
]
