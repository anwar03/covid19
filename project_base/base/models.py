from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, verbose_name=_('created by'),
                                   related_name='%(class)s_created_by')
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, verbose_name=_('updated by'),
                                   related_name='%(class)s_updated_by', null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), null=True, blank=True)

    class Meta:
        abstract = True
