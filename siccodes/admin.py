from django.contrib import admin
from . import models

admin.site.register(models.MajorGroup)
admin.site.register(models.IndustryGroup)
admin.site.register(models.IndustrySector)
admin.site.register(models.SicCode)
