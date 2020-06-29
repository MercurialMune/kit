#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django import template


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
register = template.Library()

@register.inclusion_tag('landing-page/landing-page-header-inc.html', takes_context=True)
def renderHeader(context):

    # from pprint import pprint
    # pprint(context['data'])

    return {'context':context}