from django.contrib import admin
from .models import Enregistrement
from import_export import resources,fields,widgets
from import_export.admin import ImportExportModelAdmin


class EnregistrementResource(resources.ModelResource):
    date_prelevement = fields.Field(attribute='date_prelevement', column_name='date_prelevement', widget=widgets.DateWidget('%d/%m/%y'))
    date_traitement= fields.Field(attribute='date_traitement', column_name='date_traitement', widget=widgets.DateWidget('%d/%m/%y'))
    class Meta:
        model = Enregistrement
        fields=('genre', 'code', 'date_prelevement', 'date_traitement', 'copies_ARN', 'log_copies_ARN')
        export_order =['genre', 'code',  'date_prelevement','date_traitement', 'copies_ARN', 'log_copies_ARN']
        exclude = ('id', 'creation_time', 'update_time')
        import_id_fields = ('code','date_prelevement', 'date_traitement',)

class EnregistrementAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = EnregistrementResource
    list_display=[ 'genre','code','date_prelevement','date_traitement','copies_ARN','log_copies_ARN',
                    ]





# Register your models here.
admin.site.register(Enregistrement,EnregistrementAdmin)