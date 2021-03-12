from django.urls import re_path
from .views import InfoList
urlpatterns = [
re_path(r'^(?P<version>[v1|v2]+)/infolist$',InfoList.as_view()),
]
