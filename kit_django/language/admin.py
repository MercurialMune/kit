#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib import admin

from language       import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
admin.site.register(models.Language)
