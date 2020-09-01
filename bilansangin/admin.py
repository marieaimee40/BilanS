from django.contrib import admin
from .models import Enregistrement
from import_export import resources,fields,widgets
from import_export.admin import ImportExportModelAdmin


class EnregistrementResource(resources.ModelResource):
    #date_prelevement = fields.Field(attribute='date_prelevement', column_name='date_traitement', widget=widgets.DateWidget('<date_format>'))
    class Meta:
        model = Enregistrement
        exclude = ('id', 'creation_time', 'update_time')
        import_id_fields = ('code','date_prelevement', 'date_traitement',)

class EnregistrementAdmin(ImportExportModelAdmin):
    resource_class = EnregistrementResource





# Register your models here.
admin.site.register(Enregistrement,EnregistrementAdmin)