from django.contrib import admin
from loans.models import Type, Classification, Product, Charge, Term


class TypeAdmin(admin.ModelAdmin):
    search_fields = ['type']


admin.site.register(Type, TypeAdmin)
admin.site.register([Classification, Product, Charge, Term])
