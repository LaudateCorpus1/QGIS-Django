from django import forms

from layerdefinitions.models import LayerDefinition
from layerdefinitions.file_handler import validator

from base.forms.processing_forms import ResourceBaseCleanFileForm


class ResourceFormMixin(forms.ModelForm):
    class Meta:
        model = LayerDefinition
        fields = [
            'file', 'thumbnail_image', 'name', 'url_metadata',
            'description', 'license',
        ]


class UploadForm(ResourceBaseCleanFileForm, ResourceFormMixin):
    """Upload Form."""
    def clean_file(self):
        file = super(UploadForm, self).clean_file()
        validator(file)
        return file


class UpdateForm(ResourceFormMixin):
    """Update Form."""
