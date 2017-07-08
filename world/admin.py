from django.contrib.gis import admin
from .models import WorldBorder

# Register your models here.
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
# admin.site.register(WorldBorder, admin.GeoModelAdmin)