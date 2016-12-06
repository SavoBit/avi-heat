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
from match import *


class LdapDirectorySettings(object):
    # all schemas
    admin_bind_dn_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP Admin User DN. Administrator credentials are required to search for users under user search DN or groups under group search DN."),
        required=False,
        update_allowed=True,
    )
    password_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP Admin User Password"),
        required=False,
        update_allowed=True,
    )
    user_search_dn_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP user search DN is the root of search for a given user in the LDAP directory. Only user records present in this LDAP directory sub-tree will be validated."),
        required=False,
        update_allowed=True,
    )
    user_search_scope_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP user search scope defines how deep to search for the user starting from user search DN."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['AUTH_LDAP_SCOPE_ONE', 'AUTH_LDAP_SCOPE_SUBTREE', 'AUTH_LDAP_SCOPE_BASE']),
        ],
    )
    user_id_attribute_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP user id attribute is the login attribute that uniquely identifies a single user record."),
        required=False,
        update_allowed=True,
    )
    user_attributes_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    user_attributes_schema = properties.Schema(
        properties.Schema.LIST,
        _("LDAP user attributes to fetch on a successful user bind."),
        schema=user_attributes_item_schema,
        required=False,
        update_allowed=True,
    )
    group_search_dn_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP group search DN is the root of search for a given group in the LDAP directory. Only matching groups present in this LDAP directory sub-tree will be checked for user membership."),
        required=False,
        update_allowed=True,
    )
    group_member_attribute_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP group attribute that identifies each of the group members."),
        required=False,
        update_allowed=True,
    )
    group_search_scope_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP group search scope defines how deep to search for the group starting from the group search DN."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['AUTH_LDAP_SCOPE_ONE', 'AUTH_LDAP_SCOPE_SUBTREE', 'AUTH_LDAP_SCOPE_BASE']),
        ],
    )
    group_member_is_full_dn_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Group member entries contain full DNs instead of just user id attribute values"),
        required=False,
        update_allowed=True,
    )
    group_filter_schema = properties.Schema(
        properties.Schema.STRING,
        _("Group filter is used to identify groups during search"),
        required=False,
        update_allowed=True,
    )
    ignore_referrals_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("During user or group search, ignore searching referrals."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'admin_bind_dn',
        'password',
        'user_search_dn',
        'user_search_scope',
        'user_id_attribute',
        'user_attributes',
        'group_search_dn',
        'group_member_attribute',
        'group_search_scope',
        'group_member_is_full_dn',
        'group_filter',
        'ignore_referrals',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'admin_bind_dn': admin_bind_dn_schema,
        'password': password_schema,
        'user_search_dn': user_search_dn_schema,
        'user_search_scope': user_search_scope_schema,
        'user_id_attribute': user_id_attribute_schema,
        'user_attributes': user_attributes_schema,
        'group_search_dn': group_search_dn_schema,
        'group_member_attribute': group_member_attribute_schema,
        'group_search_scope': group_search_scope_schema,
        'group_member_is_full_dn': group_member_is_full_dn_schema,
        'group_filter': group_filter_schema,
        'ignore_referrals': ignore_referrals_schema,
    }




class LdapUserBindSettings(object):
    # all schemas
    dn_template_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP user DN pattern is used to bind LDAP user after replacing the user token with real username."),
        required=False,
        update_allowed=True,
    )
    token_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP token is replaced with real user name in the user DN pattern."),
        required=False,
        update_allowed=True,
    )
    user_id_attribute_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP user id attribute is the login attribute that uniquely identifies a single user record."),
        required=False,
        update_allowed=True,
    )
    user_attributes_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    user_attributes_schema = properties.Schema(
        properties.Schema.LIST,
        _("LDAP user attributes to fetch on a successful user bind."),
        schema=user_attributes_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'dn_template',
        'token',
        'user_id_attribute',
        'user_attributes',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'dn_template': dn_template_schema,
        'token': token_schema,
        'user_id_attribute': user_id_attribute_schema,
        'user_attributes': user_attributes_schema,
    }




class HTTPClientAuthenticationParams(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("type of client authentication"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HTTP_BASIC_AUTH']),
        ],
    )
    request_uri_path_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rrequest URI path when the authentication applies"),
        schema=StringMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    auth_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Auth Profile to use for validating users You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    realm_schema = properties.Schema(
        properties.Schema.STRING,
        _("Basic authentication realm to present to a user along with the prompt for credentials."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'type',
        'request_uri_path',
        'auth_profile_uuid',
        'realm',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'request_uri_path': request_uri_path_schema,
        'auth_profile_uuid': auth_profile_uuid_schema,
        'realm': realm_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'auth_profile_uuid': 'authprofile',
        'request_uri_path': getattr(StringMatch, 'field_references', {}),
    }



class AuthMatchAttribute(object):
    # all schemas
    criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("rule match criteria"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['AUTH_MATCH_DOES_NOT_CONTAIN', 'AUTH_MATCH_CONTAINS']),
        ],
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    values_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    values_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=values_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'criteria',
        'name',
        'values',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'criteria': criteria_schema,
        'name': name_schema,
        'values': values_schema,
    }




class AuthTacacsPlusAttributeValuePair(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("attribute name"),
        required=False,
        update_allowed=True,
    )
    value_schema = properties.Schema(
        properties.Schema.STRING,
        _("attribute value"),
        required=False,
        update_allowed=True,
    )
    mandatory_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("mandatory"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'value',
        'mandatory',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'value': value_schema,
        'mandatory': mandatory_schema,
    }




class AuthProfileHTTPClientParams(object):
    # all schemas
    request_header_schema = properties.Schema(
        properties.Schema.STRING,
        _("Insert an HTTP header.  This field is used to define the header name.  The value of the header is set to the client's HTTP Auth user ID."),
        required=False,
        update_allowed=True,
    )
    cache_expiration_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The max allowed length of time a clients authentication is cached"),
        required=False,
        update_allowed=True,
    )
    require_user_groups_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    require_user_groups_schema = properties.Schema(
        properties.Schema.LIST,
        _("A user should be a member of these groups.  Each group is defined by the DN.  For example, CN=testgroup,OU=groups,dc=example,dc=avinetworks,DC=com"),
        schema=require_user_groups_item_schema,
        required=False,
        update_allowed=True,
    )
    group_member_is_full_dn_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Group member entries contain full DNs instead of just user id attribute values"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'request_header',
        'cache_expiration_time',
        'require_user_groups',
        'group_member_is_full_dn',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'request_header': request_header_schema,
        'cache_expiration_time': cache_expiration_time_schema,
        'require_user_groups': require_user_groups_schema,
        'group_member_is_full_dn': group_member_is_full_dn_schema,
    }




class AuthMatchGroupMembership(object):
    # all schemas
    criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("rule match criteria"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['AUTH_MATCH_DOES_NOT_CONTAIN', 'AUTH_MATCH_CONTAINS']),
        ],
    )
    groups_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    groups_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=groups_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'criteria',
        'groups',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'criteria': criteria_schema,
        'groups': groups_schema,
    }




class AuthMappingRule(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    group_match_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AuthMatchGroupMembership.properties_schema,
        required=False,
        update_allowed=True,
    )
    attribute_match_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AuthMatchAttribute.properties_schema,
        required=False,
        update_allowed=True,
    )
    assign_tenant_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['ASSIGN_ALL', 'ASSIGN_MATCHING_ATTRIBUTE_VALUE', 'ASSIGN_FROM_SELECT_LIST', 'ASSIGN_MATCHING_GROUP_NAME']),
        ],
    )
    tenant_attribute_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    tenant_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    tenant_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=tenant_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    assign_role_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['ASSIGN_ALL', 'ASSIGN_MATCHING_ATTRIBUTE_VALUE', 'ASSIGN_FROM_SELECT_LIST', 'ASSIGN_MATCHING_GROUP_NAME']),
        ],
    )
    role_attribute_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    role_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    role_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=role_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    is_superuser_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'group_match',
        'attribute_match',
        'assign_tenant',
        'tenant_attribute_name',
        'tenant_uuids',
        'assign_role',
        'role_attribute_name',
        'role_uuids',
        'is_superuser',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'group_match': group_match_schema,
        'attribute_match': attribute_match_schema,
        'assign_tenant': assign_tenant_schema,
        'tenant_attribute_name': tenant_attribute_name_schema,
        'tenant_uuids': tenant_uuids_schema,
        'assign_role': assign_role_schema,
        'role_attribute_name': role_attribute_name_schema,
        'role_uuids': role_uuids_schema,
        'is_superuser': is_superuser_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'role_uuids': 'role',
        'group_match': getattr(AuthMatchGroupMembership, 'field_references', {}),
        'attribute_match': getattr(AuthMatchAttribute, 'field_references', {}),
        'tenant_uuids': 'tenant',
    }



class TacacsPlusAuthSettings(object):
    # all schemas
    server_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    server_schema = properties.Schema(
        properties.Schema.LIST,
        _("TACACS+ server IP address"),
        schema=server_item_schema,
        required=False,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("TACACS+ server listening port"),
        required=False,
        update_allowed=True,
    )
    password_schema = properties.Schema(
        properties.Schema.STRING,
        _("TACACS+ server shared secret"),
        required=False,
        update_allowed=True,
    )
    service_schema = properties.Schema(
        properties.Schema.STRING,
        _("TACACS+ service"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['AUTH_TACACS_PLUS_SERVICE_LOGIN', 'AUTH_TACACS_PLUS_SERVICE_NASI', 'AUTH_TACACS_PLUS_SERVICE_ARAP', 'AUTH_TACACS_PLUS_SERVICE_X25', 'AUTH_TACACS_PLUS_SERVICE_PPP', 'AUTH_TACACS_PLUS_SERVICE_RCMD', 'AUTH_TACACS_PLUS_SERVICE_FWPROXY', 'AUTH_TACACS_PLUS_SERVICE_ENABLE', 'AUTH_TACACS_PLUS_SERVICE_NONE', 'AUTH_TACACS_PLUS_SERVICE_PT']),
        ],
    )
    authorization_attrs_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AuthTacacsPlusAttributeValuePair.properties_schema,
        required=True,
        update_allowed=False,
    )
    authorization_attrs_schema = properties.Schema(
        properties.Schema.LIST,
        _("TACACS+ authorization attribute value pairs"),
        schema=authorization_attrs_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'server',
        'port',
        'password',
        'service',
        'authorization_attrs',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'server': server_schema,
        'port': port_schema,
        'password': password_schema,
        'service': service_schema,
        'authorization_attrs': authorization_attrs_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'authorization_attrs': getattr(AuthTacacsPlusAttributeValuePair, 'field_references', {}),
    }



class LdapAuthSettings(object):
    # all schemas
    server_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    server_schema = properties.Schema(
        properties.Schema.LIST,
        _("LDAP server IP address"),
        schema=server_item_schema,
        required=False,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Query the LDAP servers on this port."),
        required=False,
        update_allowed=True,
    )
    security_mode_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP connection security mode."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['AUTH_LDAP_SECURE_NONE', 'AUTH_LDAP_SECURE_USE_LDAPS']),
        ],
    )
    base_dn_schema = properties.Schema(
        properties.Schema.STRING,
        _("The LDAP base DN.  For example, avinetworks,com would be DC=avinetworks,DC=com"),
        required=False,
        update_allowed=True,
    )
    bind_as_administrator_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("LDAP administrator credentials are used to search for users and group memberships."),
        required=False,
        update_allowed=True,
    )
    settings_schema = properties.Schema(
        properties.Schema.MAP,
        _("LDAP full directory configuration with administrator credentials"),
        schema=LdapDirectorySettings.properties_schema,
        required=False,
        update_allowed=True,
    )
    user_bind_schema = properties.Schema(
        properties.Schema.MAP,
        _("LDAP anonymous bind configuration"),
        schema=LdapUserBindSettings.properties_schema,
        required=False,
        update_allowed=True,
    )
    email_attribute_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP attribute that refers to user email"),
        required=False,
        update_allowed=True,
    )
    full_name_attribute_schema = properties.Schema(
        properties.Schema.STRING,
        _("LDAP attribute that refers to user's full name"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'server',
        'port',
        'security_mode',
        'base_dn',
        'bind_as_administrator',
        'settings',
        'user_bind',
        'email_attribute',
        'full_name_attribute',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'server': server_schema,
        'port': port_schema,
        'security_mode': security_mode_schema,
        'base_dn': base_dn_schema,
        'bind_as_administrator': bind_as_administrator_schema,
        'settings': settings_schema,
        'user_bind': user_bind_schema,
        'email_attribute': email_attribute_schema,
        'full_name_attribute': full_name_attribute_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'user_bind': getattr(LdapUserBindSettings, 'field_references', {}),
        'settings': getattr(LdapDirectorySettings, 'field_references', {}),
    }



class AuthProfile(AviResource):
    resource_name = "authprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the Auth Profile."),
        required=True,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of the Auth Profile."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['AUTH_PROFILE_LDAP', 'AUTH_PROFILE_TACACS_PLUS']),
        ],
    )
    ldap_schema = properties.Schema(
        properties.Schema.MAP,
        _("LDAP server and directory settings."),
        schema=LdapAuthSettings.properties_schema,
        required=False,
        update_allowed=True,
    )
    http_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP user authentication params."),
        schema=AuthProfileHTTPClientParams.properties_schema,
        required=False,
        update_allowed=True,
    )
    tacacs_plus_schema = properties.Schema(
        properties.Schema.MAP,
        _("TACACS+ settings"),
        schema=TacacsPlusAuthSettings.properties_schema,
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
        'type',
        'ldap',
        'http',
        'tacacs_plus',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'type': type_schema,
        'ldap': ldap_schema,
        'http': http_schema,
        'tacacs_plus': tacacs_plus_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'http': getattr(AuthProfileHTTPClientParams, 'field_references', {}),
        'tacacs_plus': getattr(TacacsPlusAuthSettings, 'field_references', {}),
        'ldap': getattr(LdapAuthSettings, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::AuthProfile': AuthProfile,
    }

