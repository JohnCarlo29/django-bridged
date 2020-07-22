from django.db import models
from django.utils.translation import gettext_lazy as _


class Document(models.Model):
    class Employment(models.TextChoices):
        EMPLOYED = 'Employed', _('Employed')
        NON_EMPLOYED = 'Non-Employed', _('Non-Employed')
        OFW = 'OFW', _('OFW')
        PENSIONERS = 'Pensioners', _('Pensioners')
        OTHER = 'Other', _('Other')

    document = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50, choices=Employment.choices)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('document', 'employment_type')

    def __str__(self):
        return self.document


class Collateral(models.Model):
    collateral = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.collateral
