from django.db import models
from django.utils.translation import gettext_lazy as _


class Bank(models.Model):
    class Category(models.TextChoices):
        NON_BANK = 'Non-Bank', _('Non-Bank')
        UNIVERSAL_BANK = 'Universal Bank', _('Universal Bank')
        THRIFT_BANK = 'Savings/Thrift Bank', _('Savings/Thrift Bank')
        RURAL_BANK = 'Rural Bank', _('Rural Bank')
        COOP_BANK = 'Coop Bank', _('Coop Bank')
        COOPERATIVE = 'Cooperative', _('Cooperative')
        PRIVATE_FINANCING = 'Private Financing', _('Private Financing')

    name = models.CharField(max_length=255, unique=True)
    slogan = models.CharField(max_length=255)
    logo = models.FileField()
    category = models.CharField(max_length=100, choices=Category.choices)
    description = models.TextField()
    operating_area = models.TextField()
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Branches'
        unique_together = [['bank', 'branch']]

    def __str__(self):
        return f"{self.bank.name} - {self.branch}"
