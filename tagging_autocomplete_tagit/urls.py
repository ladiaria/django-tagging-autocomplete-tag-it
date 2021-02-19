from django.conf.urls import *
from tagging_autocomplete_tagit.views import list_tags

urlpatterns = [
    url(r'^list$', list_tags, name='tagging_autocomplete_tagit-list'),
]
