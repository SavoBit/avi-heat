# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from common import *
from options import *
from rate import *
from match import *


class FailActionHTTPLocalResponse(object):
    # all schemas
    status_code_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['FAIL_HTTP_STATUS_CODE_503', 'FAIL_HTTP_STATUS_CODE_200']),
        ],
    )
    file_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPLocalFile.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'status_code',
        'file',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'status_code': status_code_schema,
        'file': file_schema,
    }




class AbPool(object):
    # all schemas
    pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Pool configured as B pool for A/B testing"),
        required=True,
        update_allowed=True,
    )
    ratio_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Ratio of traffic diverted to the B pool, for A/B testing"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'pool_uuid',
        'ratio',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': pool_uuid_schema,
        'ratio': ratio_schema,
    }




class FailActionBackupPool(object):
    # all schemas
    backup_pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Specifies the UUID of the Pool acting as backup pool."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'backup_pool_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'backup_pool_uuid': backup_pool_uuid_schema,
    }




class FailActionHTTPRedirect(object):
    # all schemas
    protocol_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HTTP', 'HTTPS']),
        ],
    )
    host_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    path_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    query_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    status_code_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HTTP_REDIRECT_STATUS_CODE_302', 'HTTP_REDIRECT_STATUS_CODE_301', 'HTTP_REDIRECT_STATUS_CODE_307']),
        ],
    )

    # properties list
    PROPERTIES = (
        'protocol',
        'host',
        'path',
        'query',
        'status_code',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'protocol': protocol_schema,
        'host': host_schema,
        'path': path_schema,
        'query': query_schema,
        'status_code': status_code_schema,
    }




class PlacementNetwork(object):
    # all schemas
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    subnet_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'network_uuid',
        'subnet',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'network_uuid': network_uuid_schema,
        'subnet': subnet_schema,
    }




class FailAction(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Enables a response to client when pool experiences a failure. By default TCP connection is closed."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['FAIL_ACTION_BACKUP_POOL', 'FAIL_ACTION_CLOSE_CONN', 'FAIL_ACTION_HTTP_LOCAL_RSP', 'FAIL_ACTION_HTTP_REDIRECT']),
        ],
    )
    redirect_schema = properties.Schema(
        properties.Schema.MAP,
        _("URL to redirect HTTP requests to when pool experiences a failure"),
        schema=FailActionHTTPRedirect.properties_schema,
        required=False,
        update_allowed=True,
    )
    local_rsp_schema = properties.Schema(
        properties.Schema.MAP,
        _("Local response to HTTP requests when pool experiences a failure"),
        schema=FailActionHTTPLocalResponse.properties_schema,
        required=False,
        update_allowed=True,
    )
    backup_pool_schema = properties.Schema(
        properties.Schema.MAP,
        _("Backup Pool when pool experiences a failure"),
        schema=FailActionBackupPool.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'type',
        'redirect',
        'local_rsp',
        'backup_pool',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'redirect': redirect_schema,
        'local_rsp': local_rsp_schema,
        'backup_pool': backup_pool_schema,
    }




class NetworkFilter(object):
    # all schemas
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    server_filter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'network_uuid',
        'server_filter',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'network_uuid': network_uuid_schema,
        'server_filter': server_filter_schema,
    }




class HTTPReselectRespCode(object):
    # all schemas
    codes_item_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=False,
    )
    codes_schema = properties.Schema(
        properties.Schema.LIST,
        _("HTTP response code to be matched."),
        schema=codes_item_schema,
        required=False,
        update_allowed=True,
    )
    ranges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPStatusRange.properties_schema,
        required=True,
        update_allowed=False,
    )
    ranges_schema = properties.Schema(
        properties.Schema.LIST,
        _("HTTP response code ranges to match."),
        schema=ranges_item_schema,
        required=False,
        update_allowed=True,
    )
    resp_code_block_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['HTTP_RSP_5XX', 'HTTP_RSP_4XX']),
        ],
    )
    resp_code_block_schema = properties.Schema(
        properties.Schema.LIST,
        _("Block of HTTP response codes to match for server reselect."),
        schema=resp_code_block_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'codes',
        'ranges',
        'resp_code_block',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'codes': codes_schema,
        'ranges': ranges_schema,
        'resp_code_block': resp_code_block_schema,
    }




class DiscoveredNetwork(object):
    # all schemas
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Discovered network for this IP."),
        required=True,
        update_allowed=True,
    )
    subnet_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=False,
    )
    subnet_schema = properties.Schema(
        properties.Schema.LIST,
        _("Discovered subnet for this IP."),
        schema=subnet_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'network_uuid',
        'subnet',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'network_uuid': network_uuid_schema,
        'subnet': subnet_schema,
    }




class HTTPServerReselect(object):
    # all schemas
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable HTTP request reselect when server responds with specific response codes."),
        required=True,
        update_allowed=True,
    )
    svr_resp_code_schema = properties.Schema(
        properties.Schema.MAP,
        _("Server response codes which will trigger an HTTP request retry."),
        schema=HTTPReselectRespCode.properties_schema,
        required=False,
        update_allowed=True,
    )
    num_retries_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of times to retry an HTTP request when server responds with configured status codes."),
        required=False,
        update_allowed=True,
    )
    retry_nonidempotent_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Allow retry of non-idempotent HTTP requests."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'enabled',
        'svr_resp_code',
        'num_retries',
        'retry_nonidempotent',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'enabled': enabled_schema,
        'svr_resp_code': svr_resp_code_schema,
        'num_retries': num_retries_schema,
        'retry_nonidempotent': retry_nonidempotent_schema,
    }




class Server(object):
    # all schemas
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the server.  Required if there is no resolvable host name."),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Optionally specify the servers port number.  This will override the pool's default server port attribute."),
        required=False,
        update_allowed=True,
    )
    hostname_schema = properties.Schema(
        properties.Schema.STRING,
        _("DNS resolvable name of the server.  May be used in place of the IP address."),
        required=False,
        update_allowed=True,
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable, Disable or Graceful Disable determine if new or existing connections to the server are allowed."),
        required=False,
        update_allowed=True,
    )
    ratio_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Overrides the default ratio of 1.  Reduces the percentage the LB algorithm would pick the server in relation to its peers.  Range is 1-20."),
        required=False,
        update_allowed=True,
    )
    vm_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    nw_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    discovered_network_uuid_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    discovered_network_uuid_schema = properties.Schema(
        properties.Schema.LIST,
        _("Discovered network for this server."),
        schema=discovered_network_uuid_item_schema,
        required=False,
        update_allowed=True,
    )
    external_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID identifying VM in OpenStack and other external compute"),
        required=False,
        update_allowed=True,
    )
    discovered_subnet_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=False,
    )
    discovered_subnet_schema = properties.Schema(
        properties.Schema.LIST,
        _("Discovered subnet for this server."),
        schema=discovered_subnet_item_schema,
        required=False,
        update_allowed=True,
    )
    verify_network_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Verify server belongs to a discovered network or reachable via a discovered network. Verify reachable network isn't the OpenStack management network"),
        required=False,
        update_allowed=True,
    )
    discovered_networks_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DiscoveredNetwork.properties_schema,
        required=True,
        update_allowed=False,
    )
    discovered_networks_schema = properties.Schema(
        properties.Schema.LIST,
        _("Discovered networks providing reachability for server IP."),
        schema=discovered_networks_item_schema,
        required=False,
        update_allowed=True,
    )
    resolve_server_by_dns_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Auto resolve server's IP using DNS name"),
        required=False,
        update_allowed=True,
    )
    prst_hdr_val_schema = properties.Schema(
        properties.Schema.STRING,
        _("Header value for custom header persistence."),
        required=False,
        update_allowed=True,
    )
    mac_address_schema = properties.Schema(
        properties.Schema.STRING,
        _("MAC address of server."),
        required=False,
        update_allowed=True,
    )
    static_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("If statically learned."),
        required=False,
        update_allowed=True,
    )
    server_node_schema = properties.Schema(
        properties.Schema.STRING,
        _("Hostname of the node where the server VM or container resides"),
        required=False,
        update_allowed=True,
    )
    availability_zone_schema = properties.Schema(
        properties.Schema.STRING,
        _("Availability-zone of the server VM."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip',
        'port',
        'hostname',
        'enabled',
        'ratio',
        'vm_uuid',
        'nw_uuid',
        'discovered_network_uuid',
        'external_uuid',
        'discovered_subnet',
        'verify_network',
        'discovered_networks',
        'resolve_server_by_dns',
        'prst_hdr_val',
        'mac_address',
        'static',
        'server_node',
        'availability_zone',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip': ip_schema,
        'port': port_schema,
        'hostname': hostname_schema,
        'enabled': enabled_schema,
        'ratio': ratio_schema,
        'vm_uuid': vm_uuid_schema,
        'nw_uuid': nw_uuid_schema,
        'discovered_network_uuid': discovered_network_uuid_schema,
        'external_uuid': external_uuid_schema,
        'discovered_subnet': discovered_subnet_schema,
        'verify_network': verify_network_schema,
        'discovered_networks': discovered_networks_schema,
        'resolve_server_by_dns': resolve_server_by_dns_schema,
        'prst_hdr_val': prst_hdr_val_schema,
        'mac_address': mac_address_schema,
        'static': static_schema,
        'server_node': server_node_schema,
        'availability_zone': availability_zone_schema,
    }




class Pool(AviResource):
    resource_name = "pool"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("The name of the pool."),
        required=True,
        update_allowed=True,
    )
    default_server_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Traffic sent to servers will use this destination server port unless overridden by the server's specific port attribute. The SSL checkbox enables Avi to server encryption."),
        required=False,
        update_allowed=True,
    )
    graceful_disable_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Used to gracefully disable a server. Virtual service waits for the specified time before terminating the existing connections  to the servers that are disabled."),
        required=False,
        update_allowed=True,
    )
    connection_ramp_duration_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Duration for which new connections will be gradually ramped up to a server recently brought online.  Useful for LB algorithms that are least connection based."),
        required=False,
        update_allowed=True,
    )
    max_concurrent_connections_per_server_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The maximum number of concurrent connections allowed to each server within the pool."),
        required=False,
        update_allowed=True,
    )
    health_monitor_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    health_monitor_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("Verify server health by applying one or more health monitors.  Active monitors generate synthetic traffic from each Service Engine and mark a server up or down based on the response. The Passive monitor listens to client to server communication and raises or lowers the ratio of traffic destined to a server based on successful responses."),
        schema=health_monitor_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    servers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=Server.properties_schema,
        required=True,
        update_allowed=False,
    )
    servers_schema = properties.Schema(
        properties.Schema.LIST,
        _("The pool directs load balanced traffic to this list of destination servers. The servers can be configured by IP address, name, network or via IP Address Group"),
        schema=servers_item_schema,
        required=False,
        update_allowed=True,
    )
    server_count_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    lb_algorithm_schema = properties.Schema(
        properties.Schema.STRING,
        _("The load balancing algorithm will pick a server within the pool's list of available servers."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LB_ALGORITHM_ROUND_ROBIN', 'LB_ALGORITHM_LEAST_LOAD', 'LB_ALGORITHM_FEWEST_TASKS', 'LB_ALGORITHM_RANDOM', 'LB_ALGORITHM_FEWEST_SERVERS', 'LB_ALGORITHM_LEAST_CONNECTIONS', 'LB_ALGORITHM_FASTEST_RESPONSE', 'LB_ALGORITHM_CONSISTENT_HASH']),
        ],
    )
    lb_algorithm_hash_schema = properties.Schema(
        properties.Schema.STRING,
        _("Criteria used as a key for determining the hash between the client and  server."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS_AND_PORT', 'LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS', 'LB_ALGORITHM_CONSISTENT_HASH_CUSTOM_HEADER', 'LB_ALGORITHM_CONSISTENT_HASH_URI']),
        ],
    )
    lb_algorithm_consistent_hash_hdr_schema = properties.Schema(
        properties.Schema.STRING,
        _("HTTP header name to be used for the hash key."),
        required=False,
        update_allowed=True,
    )
    networks_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=NetworkFilter.properties_schema,
        required=True,
        update_allowed=False,
    )
    networks_schema = properties.Schema(
        properties.Schema.LIST,
        _("Networks designated as containing servers for this pool.  The servers may be further narrowed down by a filter."),
        schema=networks_item_schema,
        required=False,
        update_allowed=True,
    )
    placement_networks_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=PlacementNetwork.properties_schema,
        required=True,
        update_allowed=False,
    )
    placement_networks_schema = properties.Schema(
        properties.Schema.LIST,
        _("Manually select the networks and subnets used to provide reachability to the pool's servers.  Specify the Subnet using the following syntax: 10.1.1.0/24"),
        schema=placement_networks_item_schema,
        required=False,
        update_allowed=True,
    )
    application_persistence_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Persistence will ensure the same user sticks to the same server for a desired duration of time."),
        required=False,
        update_allowed=True,
    )
    ssl_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("When enabled, Avi re-encrypts traffic to the backend servers. The specific SSL profile defines which ciphers and SSL versions will be supported."),
        required=False,
        update_allowed=True,
    )
    inline_health_monitor_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("The Passive monitor will monitor client to server connections and requests and adjust traffic load to servers based on successful responses.  This may alter the expected behavior of the LB method, such as Round Robin."),
        required=False,
        update_allowed=True,
    )
    use_service_port_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Do not translate the client's destination port when sending the connection to the server.  The pool or servers specified service port will still be used for health monitoring.  This feature is only applicable for a Virtual Service configured with the application type set to L4."),
        required=False,
        update_allowed=True,
    )
    fail_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Enable an action - Close Connection, HTTP Redirect, Local HTTP Response, or Backup Pool - when a pool failure happens. By default, a connection will be closed, in case the pool experiences a failure."),
        schema=FailAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    capacity_estimation_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Inline estimation of capacity of servers."),
        required=False,
        update_allowed=True,
    )
    capacity_estimation_ttfb_thresh_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The maximum time-to-first-byte of a server."),
        required=False,
        update_allowed=True,
    )
    pki_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi will validate the SSL certificate present by a server against the selected PKI Profile."),
        required=False,
        update_allowed=True,
    )
    ssl_key_and_certificate_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Service Engines will present a client SSL certificate to the server."),
        required=False,
        update_allowed=True,
    )
    server_auto_scale_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Server AutoScale. Not used anymore."),
        required=False,
        update_allowed=True,
    )
    prst_hdr_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Header name for custom header persistence"),
        required=False,
        update_allowed=True,
    )
    apic_epg_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Synchronize Cisco APIC EPG members with pool servers"),
        required=False,
        update_allowed=True,
    )
    autoscale_networks_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    autoscale_networks_schema = properties.Schema(
        properties.Schema.LIST,
        _("Network Ids for the launch configuration"),
        schema=autoscale_networks_item_schema,
        required=False,
        update_allowed=True,
    )
    autoscale_policy_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Reference to Server Autoscale Policy"),
        required=False,
        update_allowed=True,
    )
    autoscale_launch_config_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Reference to the Launch Configuration Profile"),
        required=False,
        update_allowed=True,
    )
    ipaddrgroup_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Use list of servers from Ip Address Group"),
        required=False,
        update_allowed=True,
    )
    fewest_tasks_feedback_delay_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Periodicity of feedback for fewest tasks server selection algorithm."),
        required=False,
        update_allowed=True,
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the pool.  Disabling will terminate all open connections and pause health monitors."),
        required=False,
        update_allowed=True,
    )
    max_conn_rate_per_server_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit connections to each server."),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    east_west_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Inherited config from VirtualService."),
        required=False,
        update_allowed=True,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("Creator name"),
        required=False,
        update_allowed=True,
    )
    cloud_config_cksum_schema = properties.Schema(
        properties.Schema.STRING,
        _("Checksum of cloud configuration for Pool. Internally set by cloud connector"),
        required=False,
        update_allowed=True,
    )
    request_queue_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable request queue when pool is full"),
        required=False,
        update_allowed=True,
    )
    request_queue_depth_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Minimum number of requests to be queued when pool is full."),
        required=False,
        update_allowed=True,
    )
    ab_pool_schema = properties.Schema(
        properties.Schema.MAP,
        _("A/B pool configuration."),
        schema=AbPool.properties_schema,
        required=False,
        update_allowed=True,
    )
    server_reselect_schema = properties.Schema(
        properties.Schema.MAP,
        _("Server reselect configuration for HTTP requests."),
        schema=HTTPServerReselect.properties_schema,
        required=False,
        update_allowed=True,
    )
    a_pool_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of container cloud application that constitutes A pool in a A-B pool configuration, if different from VS app"),
        required=False,
        update_allowed=True,
    )
    ab_priority_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Priority of this pool in a A-B pool pair. Internally used"),
        required=False,
        update_allowed=True,
    )
    host_check_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable host header name check for server certificate. If enabled and no explicit domain name is specified, Avi will use the incoming host header to do the match."),
        required=False,
        update_allowed=True,
    )
    domain_name_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    domain_name_schema = properties.Schema(
        properties.Schema.LIST,
        _("Comma separated list of domain names which will be used to verify the common names or subject alternative names presented by server certificates if host header check is enabled."),
        schema=domain_name_item_schema,
        required=False,
        update_allowed=True,
    )
    sni_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable TLS SNI for server connections. If disabled, Avi will not send the SNI extension as part of the handshake."),
        required=False,
        update_allowed=True,
    )
    server_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Fully qualified DNS hostname which will be used in the TLS SNI extension in server connections if SNI is enabled. If no value is specified, Avi will use the pool name instead."),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _("A description of the pool."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'default_server_port',
        'graceful_disable_timeout',
        'connection_ramp_duration',
        'max_concurrent_connections_per_server',
        'health_monitor_uuids',
        'servers',
        'server_count',
        'lb_algorithm',
        'lb_algorithm_hash',
        'lb_algorithm_consistent_hash_hdr',
        'networks',
        'placement_networks',
        'application_persistence_profile_uuid',
        'ssl_profile_uuid',
        'inline_health_monitor',
        'use_service_port',
        'fail_action',
        'capacity_estimation',
        'capacity_estimation_ttfb_thresh',
        'pki_profile_uuid',
        'ssl_key_and_certificate_uuid',
        'server_auto_scale',
        'prst_hdr_name',
        'apic_epg_name',
        'autoscale_networks',
        'autoscale_policy_uuid',
        'autoscale_launch_config_uuid',
        'ipaddrgroup_uuid',
        'fewest_tasks_feedback_delay',
        'enabled',
        'max_conn_rate_per_server',
        'east_west',
        'created_by',
        'cloud_config_cksum',
        'request_queue_enabled',
        'request_queue_depth',
        'ab_pool',
        'server_reselect',
        'a_pool',
        'ab_priority',
        'host_check_enabled',
        'domain_name',
        'sni_enabled',
        'server_name',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'default_server_port': default_server_port_schema,
        'graceful_disable_timeout': graceful_disable_timeout_schema,
        'connection_ramp_duration': connection_ramp_duration_schema,
        'max_concurrent_connections_per_server': max_concurrent_connections_per_server_schema,
        'health_monitor_uuids': health_monitor_uuids_schema,
        'servers': servers_schema,
        'server_count': server_count_schema,
        'lb_algorithm': lb_algorithm_schema,
        'lb_algorithm_hash': lb_algorithm_hash_schema,
        'lb_algorithm_consistent_hash_hdr': lb_algorithm_consistent_hash_hdr_schema,
        'networks': networks_schema,
        'placement_networks': placement_networks_schema,
        'application_persistence_profile_uuid': application_persistence_profile_uuid_schema,
        'ssl_profile_uuid': ssl_profile_uuid_schema,
        'inline_health_monitor': inline_health_monitor_schema,
        'use_service_port': use_service_port_schema,
        'fail_action': fail_action_schema,
        'capacity_estimation': capacity_estimation_schema,
        'capacity_estimation_ttfb_thresh': capacity_estimation_ttfb_thresh_schema,
        'pki_profile_uuid': pki_profile_uuid_schema,
        'ssl_key_and_certificate_uuid': ssl_key_and_certificate_uuid_schema,
        'server_auto_scale': server_auto_scale_schema,
        'prst_hdr_name': prst_hdr_name_schema,
        'apic_epg_name': apic_epg_name_schema,
        'autoscale_networks': autoscale_networks_schema,
        'autoscale_policy_uuid': autoscale_policy_uuid_schema,
        'autoscale_launch_config_uuid': autoscale_launch_config_uuid_schema,
        'ipaddrgroup_uuid': ipaddrgroup_uuid_schema,
        'fewest_tasks_feedback_delay': fewest_tasks_feedback_delay_schema,
        'enabled': enabled_schema,
        'max_conn_rate_per_server': max_conn_rate_per_server_schema,
        'east_west': east_west_schema,
        'created_by': created_by_schema,
        'cloud_config_cksum': cloud_config_cksum_schema,
        'request_queue_enabled': request_queue_enabled_schema,
        'request_queue_depth': request_queue_depth_schema,
        'ab_pool': ab_pool_schema,
        'server_reselect': server_reselect_schema,
        'a_pool': a_pool_schema,
        'ab_priority': ab_priority_schema,
        'host_check_enabled': host_check_enabled_schema,
        'domain_name': domain_name_schema,
        'sni_enabled': sni_enabled_schema,
        'server_name': server_name_schema,
        'description': description_schema,
    }




class PoolHealthMonitorUuids(AviNestedResource):
    resource_name = "pool"
    nested_property_name = "health_monitor_uuids"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pool"),
        required=True,
        update_allowed=False,
    )
    health_monitor_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('pool_uuid',
                  'health_monitor_uuids',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': parent_uuid_schema,
        'health_monitor_uuids': health_monitor_uuids_item_schema,
    }


class PoolServers(AviNestedResource, Server):
    resource_name = "pool"
    nested_property_name = "servers"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pool"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = Server.PROPERTIES + ('pool_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': parent_uuid_schema,
    }
    properties_schema.update(Server.properties_schema)


class PoolNetworks(AviNestedResource, NetworkFilter):
    resource_name = "pool"
    nested_property_name = "networks"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pool"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = NetworkFilter.PROPERTIES + ('pool_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': parent_uuid_schema,
    }
    properties_schema.update(NetworkFilter.properties_schema)


class PoolPlacementNetworks(AviNestedResource, PlacementNetwork):
    resource_name = "pool"
    nested_property_name = "placement_networks"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pool"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = PlacementNetwork.PROPERTIES + ('pool_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': parent_uuid_schema,
    }
    properties_schema.update(PlacementNetwork.properties_schema)


class PoolAutoscaleNetworks(AviNestedResource):
    resource_name = "pool"
    nested_property_name = "autoscale_networks"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pool"),
        required=True,
        update_allowed=False,
    )
    autoscale_networks_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('pool_uuid',
                  'autoscale_networks',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': parent_uuid_schema,
        'autoscale_networks': autoscale_networks_item_schema,
    }


class PoolDomainName(AviNestedResource):
    resource_name = "pool"
    nested_property_name = "domain_name"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pool"),
        required=True,
        update_allowed=False,
    )
    domain_name_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('pool_uuid',
                  'domain_name',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'pool_uuid': parent_uuid_schema,
        'domain_name': domain_name_item_schema,
    }


def resource_mapping():
    return {
        'Avi::Pool::PlacementNetwork': PoolPlacementNetworks,
        'Avi::Pool::AutoscaleNetwork': PoolAutoscaleNetworks,
        'Avi::Pool::Server': PoolServers,
        'Avi::Pool::DomainName': PoolDomainName,
        'Avi::Pool::HealthMonitorUuid': PoolHealthMonitorUuids,
        'Avi::Pool::Network': PoolNetworks,
        'Avi::Pool': Pool,
    }

