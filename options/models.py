from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from options import model_names

option_models = {}

for name in model_names:
    class_name = name.capitalize() # TODO handle camelcase properly
    bases = (models.Model,)
    attrs = {
        'name': models.CharField(max_length=255, unique=True),
        'Meta': type('Meta', (object,), {'ordering': ['name']}),
        '__unicode__': lambda self: self.name,
        '__module__': __name__,
    }
    option_models[name] = type(class_name, bases, attrs)


class Synonym(models.Model):
    name = models.CharField(max_length=255, unique=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.name
