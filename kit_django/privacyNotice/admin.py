#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib import admin

from privacyNotice  import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class PrivacyNoticeAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

admin.site.register(models.PrivacyNotice, PrivacyNoticeAdmin)
