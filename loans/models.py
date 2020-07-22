from django.db import models
from banks.models import Bank
from documents.models import Document, Collateral
from django.utils.translation import gettext_lazy as _


class Type(models.Model):
    type = models.CharField(max_length=255, verbose_name='loan type')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.type


class Classification(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    classification = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.classification


class Product(models.Model):
    class Computation(models.TextChoices):
        BALLOON = 'Balloon', _('Balloon'),
        ADD_ON = 'Add On', _('Add On'),
        DIMINISHING = 'Diminishing', _('Diminishing'),

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    documents = models.ManyToManyField(Document)
    collaterals = models.ManyToManyField(Collateral)
    name = models.CharField(max_length=255)
    description = models.TextField()
    min_loan_amount = models.IntegerField()
    max_loan_amount = models.IntegerField()
    computation = models.CharField(max_length=100, choices=Computation.choices)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    min_income = models.IntegerField()
    min_tenure = models.IntegerField()
    agreement = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Charge(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    charge_type = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.product.name} - {self.charge_type}'


class Term(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    term = models.IntegerField()
    interest_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = [['product', 'term', 'interest_rate']]
