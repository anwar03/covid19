from django.db import models
from django.utils.translation import ugettext_lazy as _


class Covid(models.Model):
    country = models.ForeignKey(to='contact.Country', on_delete=models.SET_NULL, null=True, blank=True)
    confirmed = models.IntegerField(verbose_name=_('confirmed'), default=0, null=True, blank=True)
    death = models.IntegerField(verbose_name=_('death'), default=0, null=True, blank=True)
    recovered = models.IntegerField(verbose_name=_('recovered'), default=0, null=True, blank=True)
    created_at = models.DateField(verbose_name=_('created at'), auto_now=False, auto_now_add=False,)
    latitude = models.DecimalField(verbose_name=_('latitude'), max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(verbose_name=_('longitude'), max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.country.name + ' ' + str(self.created_at)
