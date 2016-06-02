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
from common import *


class Permission(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['WRITE_ACCESS', 'READ_ACCESS', 'NO_ACCESS']),
        ],
    )
    resource_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PERMISSION_SSLPROFILE', 'PERMISSION_ROLE', 'PERMISSION_NETWORK', 'PERMISSION_AUTHPROFILE', 'PERMISSION_POOL', 'PERMISSION_ALERT', 'PERMISSION_VIRTUALSERVICE_MAINTENANCE', 'PERMISSION_MICROSERVICEGROUP', 'PERMISSION_ALERTSYSLOGCONFIG', 'PERMISSION_EXEMPT', 'PERMISSION_ANALYTICSPROFILE', 'PERMISSION_HTTPPOLICYSET', 'PERMISSION_VRFCONTEXT', 'PERMISSION_APPLICATIONPROFILE', 'PERMISSION_NETWORKSECURITYPOLICY', 'PERMISSION_VSDATASCRIPTSET', 'PERMISSION_TECHSUPPORT', 'PERMISSION_ALERTCONFIG', 'PERMISSION_NETWORKPROFILE', 'PERMISSION_SERVICEENGINEGROUP', 'PERMISSION_UPGRADE', 'PERMISSION_INTERNAL', 'PERMISSION_APPLICATIONPERSISTENCEPROFILE', 'PERMISSION_SNMPTRAPPROFILE', 'PERMISSION_ACTIONGROUPCONFIG', 'PERMISSION_REBOOT', 'PERMISSION_SSLKEYANDCERTIFICATE', 'PERMISSION_CONTROLLER', 'PERMISSION_IPAMDNSPROVIDERPROFILE', 'PERMISSION_HEALTHMONITOR', 'PERMISSION_ALERTEMAILCONFIG', 'PERMISSION_CERTIFICATEMANAGEMENTPROFILE', 'PERMISSION_SERVICEENGINE', 'PERMISSION_TENANT', 'PERMISSION_TRAFFIC_CAPTURE', 'PERMISSION_USER', 'PERMISSION_VIRTUALSERVICE', 'PERMISSION_PKIPROFILE', 'PERMISSION_CLOUD', 'PERMISSION_IPADDRGROUP', 'PERMISSION_SYSTEMCONFIGURATION', 'PERMISSION_POOL_MAINTENANCE', 'PERMISSION_STRINGGROUP']),
        ],
    )

    # properties list
    PROPERTIES = (
        'type',
        'resource',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'resource': resource_schema,
    }




class Role(AviResource):
    resource_name = "role"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    privileges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=Permission.properties_schema,
        required=True,
        update_allowed=False,
    )
    privileges_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=privileges_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'privileges',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'privileges': privileges_schema,
    }




class RolePrivileges(AviNestedResource, Permission):
    resource_name = "role"
    nested_property_name = "privileges"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of role"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = Permission.PROPERTIES + ('role_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'role_uuid': parent_uuid_schema,
    }
    properties_schema.update(Permission.properties_schema)


def resource_mapping():
    return {
        'Avi::Role::Privilege': RolePrivileges,
        'Avi::Role': Role,
    }

