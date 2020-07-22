from django.db import IntegrityError
from import_export import fields, resources
from .models import Branch, Bank


class BranchResource(resources.ModelResource):
    class Meta:
        model = Branch
        skip_unchanged = True
        exclude = ('created_at', 'updated_at')

    def __init__(self, bank=None):
        super()
        self.bank = bank

    def before_import_row(self, row, **kwargs):
        row['bank'] = self.bank

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super().save_instance(instance, using_transactions, dry_run)
        except IntegrityError:
            pass
