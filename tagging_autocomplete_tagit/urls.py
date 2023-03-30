from django.urls import re_path
from tagging_autocomplete_tagit.views import list_tags

urlpatterns = [
    re_path(r'^list$', list_tags, name='tagging_autocomplete_tagit-list'),
]
