from django.db import models
from tagging.fields import TagField
from tagging_autocomplete.widgets import TagAutocomplete
from django.contrib.admin.widgets import AdminTextInputWidget

# The following code is based on models.py file from django-tinymce by Joost Cassee

class TagAutocompleteField(TagField):
    """
    TagField with autocomplete widget
    """
    
    def __init__(self, max_tags=False, *args, **kwargs):
        self.max_tags = max_tags
        super(TagAutocompleteField, self).__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        defaults = {'widget': TagAutocomplete(max_tags=self.max_tags)}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == AdminTextInputWidget:
            defaults['widget'] = TagAutocomplete(max_tags=self.max_tags)

        return super(TagAutocompleteField, self).formfield(**defaults)
