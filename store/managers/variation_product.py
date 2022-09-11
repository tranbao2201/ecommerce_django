from django.db import models
from store.models import VariationType
from django.db.models.query import QuerySet


class VariationProductQuerySet(QuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class VariationProductManager(models.Manager):
    def get_queryset(self):
        return VariationProductQuerySet(self.model, using=self._db).filter(is_active=True)

    def include_deactivate(self, *args, **kwargs):
        return VariationProductQuerySet(self.model, using=self._db)

    def only_sizes(self):
        return self.get_queryset().filter(variation_type=VariationType.SIZE)

    def only_colors(self):
        return self.get_queryset().filter(variation_type=VariationType.COLOR)
