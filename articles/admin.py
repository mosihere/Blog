from django.contrib import admin
from . import models


# Register your models here.

#  After Creating a Model ( class ) in models.py
# we have to register and submit our model in admin.py
# admin.site.register(models.ModelsName)
admin.site.register(models.Articles)
