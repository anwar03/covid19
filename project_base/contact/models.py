from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'(^[+0-9]{1,3})*([0-9]{10,11}$)', message="Enter your valid contact number.")
    email = models.EmailField(verbose_name=_('email'), null=True, blank=True)
    mobile = models.CharField(validators=[phone_regex], verbose_name=_('mobile'), max_length=20, null=True, blank=True)
    telephone = models.CharField(validators=[phone_regex], verbose_name=_('telephone'), max_length=20, null=True, blank=True)

    def __str__(self):
        return self.email


class Country(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    country_code2 = models.CharField(verbose_name=_('country code'), max_length=3, null=True, blank=True)
    dialing_code = models.CharField(verbose_name=_('dialing code'), max_length=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Address(models.Model):
    line1 = models.CharField(verbose_name=_('address line1'), max_length=255, null=True, blank=True)
    line2 = models.CharField(verbose_name=_('address line2'), max_length=255, null=True, blank=True)
    zip = models.CharField(verbose_name=_('zip'), max_length=20, null=True, blank=True)
    state = models.CharField(verbose_name=_('state'), max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name=_('city'), max_length=100, null=True, blank=True)
    country = models.ForeignKey(to='contact.Country', verbose_name=_('country'), related_name='addresses',
                                on_delete=models.CASCADE)
    lat = models.DecimalField(verbose_name=_('latitude'), max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(verbose_name=_('longitude'), max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return (self.line1 + '') if self.line1 else '' + \
                (self.line2 + ' ') if self.line2 else '' + \
                (self.zip + ' ') if self.zip else '' + \
                (self.city + ' ') if self.city else '' + \
                self.country.name if self.country else ''
