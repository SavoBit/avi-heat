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
from debug_controller import *


class DebugSeAgent(object):
    # all schemas
    sub_module_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['VI_MGR_DEBUG', 'HS_MGR_DEBUG', 'SE_MGR_DEBUG', 'SE_AGENT_DEBUG', 'RPC_INFRA_DEBUG', 'SE_AGENT_METRICS_DEBUG', 'TASK_QUEUE_DEBUG', 'TRANSACTION_DEBUG', 'METRICS_MANAGER_DEBUG', 'AUTOSCALE_MGR_DEBUG', 'RES_MGR_DEBUG', 'ALERT_MGR_DEBUG', 'REDIS_INFRA_DEBUG', 'APIC_AGENT_DEBUG', 'MESOS_METRICS_DEBUG', 'CLOUD_CONNECTOR_DEBUG', 'METRICS_MGR_DEBUG', 'VIRTUALSERVICE_DEBUG', 'STATECACHE_MGR_DEBUG', 'EVENT_API_DEBUG', 'JOB_MGR_DEBUG']),
        ],
    )
    trace_level_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['TRACE_LEVEL_DEBUG', 'TRACE_LEVEL_ERROR', 'TRACE_LEVEL_DISABLED', 'TRACE_LEVEL_DEBUG_DETAIL']),
        ],
    )
    log_level_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LOG_LEVEL_ERROR', 'LOG_LEVEL_DISABLED', 'LOG_LEVEL_INFO', 'LOG_LEVEL_WARNING']),
        ],
    )

    # properties list
    PROPERTIES = (
        'sub_module',
        'trace_level',
        'log_level',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'sub_module': sub_module_schema,
        'trace_level': trace_level_schema,
        'log_level': log_level_schema,
    }




class DebugSeDataplane(object):
    # all schemas
    flag_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DEBUG_STRICT', 'DEBUG_ETHERNET_PKT_OUT', 'DEBUG_ARP_PKT_OUT', 'DEBUG_ALL', 'DEBUG_PCAP_RX', 'DEBUG_IP_PKT_OUT', 'DEBUG_ARP_PKT_IN', 'DEBUG_POOL', 'DEBUG_MISC', 'DEBUG_CRUD', 'DEBUG_PCAP_HM', 'DEBUG_PCAP_ALL', 'DEBUG_DISPATCHER_FLOW_DETAIL', 'DEBUG_UDP', 'DEBUG_PCAP_DOS', 'DEBUG_PCAP_DROP', 'DEBUG_NONE', 'DEBUG_DISPATCHER_FLOW', 'DEBUG_ICMP', 'DEBUG_ERROR', 'DEBUG_ARP', 'DEBUG_SE_APP', 'DEBUG_ETHERNET', 'DEBUG_IP_PKT_IN', 'DEBUG_ETHERNET_PKT_IN', 'DEBUG_IP', 'DEBUG_PCAP_TX', 'DEBUG_CONFIG', 'DEBUG_DISPATCHER_FLOW_ALL']),
        ],
    )

    # properties list
    PROPERTIES = (
        'flag',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'flag': flag_schema,
    }




class DebugSeCpuShares(object):
    # all schemas
    cpu_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    shares_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'cpu',
        'shares',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'cpu': cpu_schema,
        'shares': shares_schema,
    }




class DebugServiceEngine(AviResource):
    resource_name = "debugserviceengine"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    seagent_debug_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugSeAgent.properties_schema,
        required=True,
        update_allowed=False,
    )
    seagent_debug_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=seagent_debug_item_schema,
        required=False,
        update_allowed=True,
    )
    flags_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugSeDataplane.properties_schema,
        required=True,
        update_allowed=False,
    )
    flags_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=flags_item_schema,
        required=False,
        update_allowed=True,
    )
    cpu_shares_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugSeCpuShares.properties_schema,
        required=True,
        update_allowed=False,
    )
    cpu_shares_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=cpu_shares_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'seagent_debug',
        'flags',
        'cpu_shares',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'seagent_debug': seagent_debug_schema,
        'flags': flags_schema,
        'cpu_shares': cpu_shares_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'flags': getattr(DebugSeDataplane, 'field_references', {}),
        'seagent_debug': getattr(DebugSeAgent, 'field_references', {}),
        'cpu_shares': getattr(DebugSeCpuShares, 'field_references', {}),
    }



class DebugIpAddr(object):
    # all schemas
    addrs_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    addrs_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=addrs_item_schema,
        required=False,
        update_allowed=True,
    )
    ranges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrRange.properties_schema,
        required=True,
        update_allowed=False,
    )
    ranges_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=ranges_item_schema,
        required=False,
        update_allowed=True,
    )
    prefixes_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=False,
    )
    prefixes_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=prefixes_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'addrs',
        'ranges',
        'prefixes',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'addrs': addrs_schema,
        'ranges': ranges_schema,
        'prefixes': prefixes_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ranges': getattr(IpAddrRange, 'field_references', {}),
        'prefixes': getattr(IpAddrPrefix, 'field_references', {}),
        'addrs': getattr(IpAddr, 'field_references', {}),
    }



class DebugVirtualServiceSeParams(object):
    # all schemas
    se_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    se_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_uuids_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'se_uuids',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'se_uuids': se_uuids_schema,
    }




class DebugVirtualServiceCapture(object):
    # all schemas
    pkt_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of bytes of each packet to capture. Use 0 to capture the entire packet."),
        required=False,
        update_allowed=True,
    )
    duration_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of minutes to capture packets. Use 0 to capture until manually stopped."),
        required=False,
        update_allowed=True,
    )
    num_pkts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Total number of packets to capture."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'pkt_size',
        'duration',
        'num_pkts',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'pkt_size': pkt_size_schema,
        'duration': duration_schema,
        'num_pkts': num_pkts_schema,
    }




class DebugVsDataplane(object):
    # all schemas
    flag_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DEBUG_VS_UDP', 'DEBUG_VS_HTTP_ALL', 'DEBUG_VS_TCP_REXMT', 'DEBUG_VS_TCP_CONNECTION', 'DEBUG_VS_PROXY_CONNECTION', 'DEBUG_VS_TCP_PKT', 'DEBUG_VS_TCP_TIMER', 'DEBUG_VS_EVENTS', 'DEBUG_VS_HM_EXT', 'DEBUG_VS_HTTP_RULES', 'DEBUG_VS_PROXY_ERR', 'DEBUG_VS_TCP_APP_PKT', 'DEBUG_VS_HM', 'DEBUG_VS_CONFIG', 'DEBUG_VS_TCP_RETRANSMIT', 'DEBUG_VS_TCP_ALL', 'DEBUG_VS_TCP_APP', 'DEBUG_VS_TCP_PKT_ERROR', 'DEBUG_VS_ALL', 'DEBUG_VS_HTTP_CORE', 'DEBUG_VS_HM_ERR', 'DEBUG_VS_PROXY_PKT', 'DEBUG_VS_SSL', 'DEBUG_VS_HM_PKT', 'DEBUG_VS_ERROR', 'DEBUG_VS_TCP_CONN_ERROR', 'DEBUG_VS_NONE', 'DEBUG_VS_CREDIT', 'DEBUG_VS_UDP_PKT']),
        ],
    )

    # properties list
    PROPERTIES = (
        'flag',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'flag': flag_schema,
    }




class DebugVirtualService(AviResource):
    resource_name = "debugvirtualservice"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    flags_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugVsDataplane.properties_schema,
        required=True,
        update_allowed=False,
    )
    flags_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=flags_item_schema,
        required=False,
        update_allowed=True,
    )
    debug_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugIpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    capture_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    capture_params_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugVirtualServiceCapture.properties_schema,
        required=False,
        update_allowed=True,
    )
    se_params_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DebugVirtualServiceSeParams.properties_schema,
        required=False,
        update_allowed=True,
    )
    debug_hm_schema = properties.Schema(
        properties.Schema.STRING,
        _("This option controls the capture of Health Monitor flows."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DEBUG_VS_HM_NONE', 'DEBUG_VS_HM_INCLUDE', 'DEBUG_VS_HM_ONLY']),
        ],
    )

    # properties list
    PROPERTIES = (
        'name',
        'flags',
        'debug_ip',
        'capture',
        'capture_params',
        'se_params',
        'debug_hm',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'flags': flags_schema,
        'debug_ip': debug_ip_schema,
        'capture': capture_schema,
        'capture_params': capture_params_schema,
        'se_params': se_params_schema,
        'debug_hm': debug_hm_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'capture_params': getattr(DebugVirtualServiceCapture, 'field_references', {}),
        'debug_ip': getattr(DebugIpAddr, 'field_references', {}),
        'flags': getattr(DebugVsDataplane, 'field_references', {}),
        'se_params': getattr(DebugVirtualServiceSeParams, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::DebugVirtualService': DebugVirtualService,
        'Avi::LBaaS::DebugServiceEngine': DebugServiceEngine,
    }

