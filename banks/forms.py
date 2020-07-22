from django import forms
from .models import Bank
from import_export.forms import ImportForm
from import_export.forms import ConfirmImportForm


class BranchImportForm(ImportForm):
    bank = forms.ModelChoiceField(
        queryset=Bank.objects.all(),
        required=True)


class BranchConfirmImportForm(ConfirmImportForm):
    bank = forms.ModelChoiceField(
        queryset=Bank.objects.all(),
        required=True)
