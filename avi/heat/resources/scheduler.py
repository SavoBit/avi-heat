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


class Scheduler(AviResource):
    resource_name = "scheduler"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of scheduler"),
        required=True,
        update_allowed=True,
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(" (Default: True)"),
        required=False,
        update_allowed=True,
    )
    run_mode_schema = properties.Schema(
        properties.Schema.STRING,
        _("Scheduler Run Mode"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['RUN_MODE_AT', 'RUN_MODE_NOW', 'RUN_MODE_PERIODIC']),
        ],
    )
    start_date_time_schema = properties.Schema(
        properties.Schema.STRING,
        _("Scheduler start date and time"),
        required=False,
        update_allowed=True,
    )
    end_date_time_schema = properties.Schema(
        properties.Schema.STRING,
        _("Scheduler end date and time"),
        required=False,
        update_allowed=True,
    )
    frequency_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Frequency at which CUSTOM scheduler will run"),
        required=False,
        update_allowed=True,
    )
    frequency_unit_schema = properties.Schema(
        properties.Schema.STRING,
        _("Unit at which CUSTOM scheduler will run"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SCHEDULER_FREQUENCY_UNIT_DAY', 'SCHEDULER_FREQUENCY_UNIT_HOUR', 'SCHEDULER_FREQUENCY_UNIT_MIN', 'SCHEDULER_FREQUENCY_UNIT_MONTH', 'SCHEDULER_FREQUENCY_UNIT_WEEK']),
        ],
    )
    backup_config_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Backup Configuration to be executed by this scheduler You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    run_script_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Control script to be executed by this scheduler You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    scheduler_action_schema = properties.Schema(
        properties.Schema.STRING,
        _("Define Scheduler Action (Default: SCHEDULER_ACTION_BACKUP)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SCHEDULER_ACTION_BACKUP', 'SCHEDULER_ACTION_RUN_A_SCRIPT']),
        ],
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'enabled',
        'run_mode',
        'start_date_time',
        'end_date_time',
        'frequency',
        'frequency_unit',
        'backup_config_uuid',
        'run_script_uuid',
        'scheduler_action',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'enabled': enabled_schema,
        'run_mode': run_mode_schema,
        'start_date_time': start_date_time_schema,
        'end_date_time': end_date_time_schema,
        'frequency': frequency_schema,
        'frequency_unit': frequency_unit_schema,
        'backup_config_uuid': backup_config_uuid_schema,
        'run_script_uuid': run_script_uuid_schema,
        'scheduler_action': scheduler_action_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'run_script_uuid': 'alertscriptconfig',
        'backup_config_uuid': 'backupconfiguration',
    }



class BackupConfiguration(AviResource):
    resource_name = "backupconfiguration"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of backup configuration."),
        required=True,
        update_allowed=True,
    )
    save_local_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Local Backup"),
        required=False,
        update_allowed=True,
    )
    maximum_backups_stored_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Rotate the backup files based on this count. (Default: 4)"),
        required=False,
        update_allowed=True,
    )
    upload_to_remote_host_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Remote Backup"),
        required=False,
        update_allowed=True,
    )
    ssh_user_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Access Credentials for remote destination. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    remote_directory_schema = properties.Schema(
        properties.Schema.STRING,
        _("Directory at remote destination with write permission for ssh user."),
        required=False,
        update_allowed=True,
    )
    remote_hostname_schema = properties.Schema(
        properties.Schema.STRING,
        _("Remote Destination."),
        required=False,
        update_allowed=True,
    )
    backup_passphrase_schema = properties.Schema(
        properties.Schema.STRING,
        _("Passphrase of backup configuration"),
        required=False,
        update_allowed=True,
    )
    backup_file_prefix_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Prefix of the exported configuration file"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'save_local',
        'maximum_backups_stored',
        'upload_to_remote_host',
        'ssh_user_uuid',
        'remote_directory',
        'remote_hostname',
        'backup_passphrase',
        'backup_file_prefix',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'save_local': save_local_schema,
        'maximum_backups_stored': maximum_backups_stored_schema,
        'upload_to_remote_host': upload_to_remote_host_schema,
        'ssh_user_uuid': ssh_user_uuid_schema,
        'remote_directory': remote_directory_schema,
        'remote_hostname': remote_hostname_schema,
        'backup_passphrase': backup_passphrase_schema,
        'backup_file_prefix': backup_file_prefix_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ssh_user_uuid': 'cloudconnectoruser',
    }



def resource_mapping():
    return {
        'Avi::LBaaS::Scheduler': Scheduler,
        'Avi::LBaaS::BackupConfiguration': BackupConfiguration,
    }

