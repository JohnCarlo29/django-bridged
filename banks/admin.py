from django.contrib import admin
from banks.forms import BranchImportForm, BranchConfirmImportForm
from banks.models import Bank, Branch
from import_export.admin import ImportExportModelAdmin
from banks.resources import BranchResource


class BranchAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BranchResource

    def get_import_form(self):
        return BranchImportForm

    def get_confirm_import_form(self):
        return BranchConfirmImportForm

    def get_form_kwargs(self, form, *args, **kwargs):
        # pass on `bank` to the kwargs for the custom confirm form
        if isinstance(form, BranchImportForm):
            if form.is_valid():
                bank = form.cleaned_data['bank']
                kwargs.update({'bank': bank.id})
        return kwargs

    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        if request.POST:
            rk['bank'] = request.POST.get('bank', None)
        print(rk)
        return rk


admin.site.register(Bank)
admin.site.register(Branch, BranchAdmin)
