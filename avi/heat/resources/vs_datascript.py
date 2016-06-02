# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *


class VSDataScript(object):
    # all schemas
    evt_schema = properties.Schema(
        properties.Schema.STRING,
        _("Event triggering execution of datascript"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['VS_DATASCRIPT_EVT_HTTP_RESP', 'VS_DATASCRIPT_EVT_HTTP_REQ', 'VS_DATASCRIPT_EVT_HTTP_LB_FAILED', 'VS_DATASCRIPT_EVT_HTTP_RESP_DATA', 'VS_DATASCRIPT_EVT_MAX']),
        ],
    )
    script_schema = properties.Schema(
        properties.Schema.STRING,
        _("Datascript to execute when the event triggers"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'evt',
        'script',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'evt': evt_schema,
        'script': script_schema,
    }




class VSDataScripts(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the virtual service datascript collection"),
        required=True,
        update_allowed=True,
    )
    vs_datascript_set_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the virtual service datascript collection"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'vs_datascript_set_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'vs_datascript_set_uuid': vs_datascript_set_uuid_schema,
    }




class VSDataScriptSet(AviResource):
    resource_name = "vsdatascriptset"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name for the virtual service datascript collection"),
        required=True,
        update_allowed=True,
    )
    datascript_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VSDataScript.properties_schema,
        required=True,
        update_allowed=False,
    )
    datascript_schema = properties.Schema(
        properties.Schema.LIST,
        _("DataScripts to execute"),
        schema=datascript_item_schema,
        required=False,
        update_allowed=True,
    )
    pool_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    pool_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("UUID of pools that could be referred by VSDataScriptSet objects."),
        schema=pool_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'datascript',
        'pool_uuids',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'datascript': datascript_schema,
        'pool_uuids': pool_uuids_schema,
        'description': description_schema,
    }




class VSDataScriptSetDatascript(AviNestedResource, VSDataScript):
    resource_name = "vsdatascriptset"
    nested_property_name = "datascript"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of vsdatascriptset"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = VSDataScript.PROPERTIES + ('vsdatascriptset_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'vsdatascriptset_uuid': parent_uuid_schema,
    }
    properties_schema.update(VSDataScript.properties_schema)


class VSDataScriptSetPoolUuids(AviNestedResource):
    resource_name = "vsdatascriptset"
    nested_property_name = "pool_uuids"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of vsdatascriptset"),
        required=True,
        update_allowed=False,
    )
    pool_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('vsdatascriptset_uuid',
                  'pool_uuids',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'vsdatascriptset_uuid': parent_uuid_schema,
        'pool_uuids': pool_uuids_item_schema,
    }


def resource_mapping():
    return {
        'Avi::VSDataScriptSet::Datascript': VSDataScriptSetDatascript,
        'Avi::VSDataScriptSet': VSDataScriptSet,
        'Avi::VSDataScriptSet::PoolUuid': VSDataScriptSetPoolUuids,
    }

