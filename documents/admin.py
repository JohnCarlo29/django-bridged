from django.contrib import admin
from documents.models import Document, Collateral

admin.site.register([Document, Collateral])
