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
from ssl_cipher_enums import *


class SSLKeyRSAParams(object):
    # all schemas
    key_size_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SSL_KEY_1024_BITS', 'SSL_KEY_2048_BITS', 'SSL_KEY_4096_BITS', 'SSL_KEY_3072_BITS']),
        ],
    )
    exponent_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'key_size',
        'exponent',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'key_size': key_size_schema,
        'exponent': exponent_schema,
    }




class SSLVersion(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SSL_VERSION_TLS1_1', 'SSL_VERSION_TLS1', 'SSL_VERSION_TLS1_2']),
        ],
    )

    # properties list
    PROPERTIES = (
        'type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
    }




class SSLKeyECParams(object):
    # all schemas
    curve_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SSL_KEY_EC_CURVE_SECP521R1', 'SSL_KEY_EC_CURVE_SECP256R1', 'SSL_KEY_EC_CURVE_SECP384R1']),
        ],
    )

    # properties list
    PROPERTIES = (
        'curve',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'curve': curve_schema,
    }




class SSLCertificateDescription(object):
    # all schemas
    common_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    email_address_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    organization_unit_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    organization_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    locality_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    state_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    country_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    distinguished_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'common_name',
        'email_address',
        'organization_unit',
        'organization',
        'locality',
        'state',
        'country',
        'distinguished_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'common_name': common_name_schema,
        'email_address': email_address_schema,
        'organization_unit': organization_unit_schema,
        'organization': organization_schema,
        'locality': locality_schema,
        'state': state_schema,
        'country': country_schema,
        'distinguished_name': distinguished_name_schema,
    }




class CertificateManagementProfile(AviResource):
    resource_name = "certificatemanagementprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the PKI Profile"),
        required=True,
        update_allowed=True,
    )
    script_params_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CustomParams.properties_schema,
        required=True,
        update_allowed=False,
    )
    script_params_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=script_params_item_schema,
        required=False,
        update_allowed=True,
    )
    script_path_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'script_params',
        'script_path',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'script_params': script_params_schema,
        'script_path': script_path_schema,
    }




class CertificateManagementProfileScriptParams(AviNestedResource):
    resource_name = "certificatemanagementprofile"
    nested_property_name = "script_params"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of certificatemanagementprofile"),
        required=True,
        update_allowed=False,
    )
    script_params_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('certificatemanagementprofile_uuid',
                  'script_params',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'certificatemanagementprofile_uuid': parent_uuid_schema,
        'script_params': script_params_item_schema,
    }


class SSLRating(object):
    # all schemas
    security_score_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    performance_rating_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SSL_SCORE_GOOD', 'SSL_SCORE_BAD', 'SSL_SCORE_EXCELLENT', 'SSL_SCORE_VERY_BAD', 'SSL_SCORE_NOT_SECURE', 'SSL_SCORE_AVERAGE']),
        ],
    )
    compatibility_rating_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SSL_SCORE_GOOD', 'SSL_SCORE_BAD', 'SSL_SCORE_EXCELLENT', 'SSL_SCORE_VERY_BAD', 'SSL_SCORE_NOT_SECURE', 'SSL_SCORE_AVERAGE']),
        ],
    )

    # properties list
    PROPERTIES = (
        'security_score',
        'performance_rating',
        'compatibility_rating',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'security_score': security_score_schema,
        'performance_rating': performance_rating_schema,
        'compatibility_rating': compatibility_rating_schema,
    }




class CRL(object):
    # all schemas
    server_url_schema = properties.Schema(
        properties.Schema.STRING,
        _("URL of a server that issues the Certificate Revocation list. If this is configured, CRL will be periodically downloaded either based on the configured update interval or the next update interval in the CRL. CRL itself is stored in the body."),
        required=False,
        update_allowed=True,
    )
    body_schema = properties.Schema(
        properties.Schema.STRING,
        _("Certificate Revocation list from a given issuer in PEM format. This can either be configured directly or via the server_url. "),
        required=False,
        update_allowed=True,
    )
    last_update_schema = properties.Schema(
        properties.Schema.STRING,
        _("The date when this CRL was last issued"),
        required=False,
        update_allowed=True,
    )
    next_update_schema = properties.Schema(
        properties.Schema.STRING,
        _("The date when a newer CRL will be available. Also conveys the date after which the CRL should be considered obsolete."),
        required=False,
        update_allowed=True,
    )
    update_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Interval in minutes to check for CRL update. If not specified, interval will be 1 day"),
        required=False,
        update_allowed=True,
    )
    etag_schema = properties.Schema(
        properties.Schema.STRING,
        _("Cached etag to optimize the download of the CRL"),
        required=False,
        update_allowed=True,
    )
    text_schema = properties.Schema(
        properties.Schema.STRING,
        _("Certificate Revocation list in plain text for readability"),
        required=False,
        update_allowed=True,
    )
    common_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Common name of the issuer in the Certificate Revocation list"),
        required=False,
        update_allowed=True,
    )
    fingerprint_schema = properties.Schema(
        properties.Schema.STRING,
        _("Fingerprint of the CRL. Used to avoid configuring duplicates"),
        required=False,
        update_allowed=True,
    )
    distinguished_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Distinguished name of the issuer in the Certificate Revocation list"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'server_url',
        'body',
        'last_update',
        'next_update',
        'update_interval',
        'etag',
        'text',
        'common_name',
        'fingerprint',
        'distinguished_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'server_url': server_url_schema,
        'body': body_schema,
        'last_update': last_update_schema,
        'next_update': next_update_schema,
        'update_interval': update_interval_schema,
        'etag': etag_schema,
        'text': text_schema,
        'common_name': common_name_schema,
        'fingerprint': fingerprint_schema,
        'distinguished_name': distinguished_name_schema,
    }




class SSLKeyParams(object):
    # all schemas
    algorithm_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SSL_KEY_ALGORITHM_RSA', 'SSL_KEY_ALGORITHM_EC']),
        ],
    )
    rsa_params_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLKeyRSAParams.properties_schema,
        required=False,
        update_allowed=True,
    )
    ec_params_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLKeyECParams.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'algorithm',
        'rsa_params',
        'ec_params',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'algorithm': algorithm_schema,
        'rsa_params': rsa_params_schema,
        'ec_params': ec_params_schema,
    }




class SSLProfile(AviResource):
    resource_name = "sslprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    accepted_versions_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLVersion.properties_schema,
        required=True,
        update_allowed=False,
    )
    accepted_versions_schema = properties.Schema(
        properties.Schema.LIST,
        _("Set of versions accepted by the server"),
        schema=accepted_versions_item_schema,
        required=False,
        update_allowed=True,
    )
    accepted_ciphers_schema = properties.Schema(
        properties.Schema.STRING,
        _("Ciphers suites represented as defined by http://www.openssl.org/docs/apps/ciphers.html"),
        required=False,
        update_allowed=True,
    )
    cipher_enums_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_RSA_WITH_AES_128_CBC_SHA', 'TLS_RSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'TLS_RSA_WITH_3DES_EDE_CBC_SHA', 'TLS_RSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA', 'TLS_RSA_WITH_RC4_128_SHA', 'TLS_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256', 'TLS_RSA_WITH_AES_256_CBC_SHA256', 'TLS_RSA_WITH_AES_256_CBC_SHA', 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA']),
        ],
    )
    cipher_enums_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=cipher_enums_item_schema,
        required=False,
        update_allowed=True,
    )
    tags_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=Tag.properties_schema,
        required=True,
        update_allowed=False,
    )
    tags_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=tags_item_schema,
        required=False,
        update_allowed=True,
    )
    ssl_rating_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLRating.properties_schema,
        required=False,
        update_allowed=True,
    )
    send_close_notify_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Send 'close notify' alert message for a clean shutdown of the SSL connection."),
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
        'accepted_versions',
        'accepted_ciphers',
        'cipher_enums',
        'tags',
        'ssl_rating',
        'send_close_notify',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'accepted_versions': accepted_versions_schema,
        'accepted_ciphers': accepted_ciphers_schema,
        'cipher_enums': cipher_enums_schema,
        'tags': tags_schema,
        'ssl_rating': ssl_rating_schema,
        'send_close_notify': send_close_notify_schema,
        'description': description_schema,
    }




class SSLProfileAcceptedVersions(AviNestedResource, SSLVersion):
    resource_name = "sslprofile"
    nested_property_name = "accepted_versions"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of sslprofile"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = SSLVersion.PROPERTIES + ('sslprofile_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'sslprofile_uuid': parent_uuid_schema,
    }
    properties_schema.update(SSLVersion.properties_schema)


class SSLProfileCipherEnums(AviNestedResource):
    resource_name = "sslprofile"
    nested_property_name = "cipher_enums"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of sslprofile"),
        required=True,
        update_allowed=False,
    )
    cipher_enums_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('sslprofile_uuid',
                  'cipher_enums',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'sslprofile_uuid': parent_uuid_schema,
        'cipher_enums': cipher_enums_item_schema,
    }


class SSLProfileTags(AviNestedResource):
    resource_name = "sslprofile"
    nested_property_name = "tags"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of sslprofile"),
        required=True,
        update_allowed=False,
    )
    tags_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = ('sslprofile_uuid',
                  'tags',
                 )

    # mapping of properties to their schemas
    properties_schema = {
        'sslprofile_uuid': parent_uuid_schema,
        'tags': tags_item_schema,
    }


class SSLCertificate(object):
    # all schemas
    version_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    serial_number_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    self_signed_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    issuer_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLCertificateDescription.properties_schema,
        required=False,
        update_allowed=True,
    )
    subject_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLCertificateDescription.properties_schema,
        required=False,
        update_allowed=True,
    )
    key_params_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLKeyParams.properties_schema,
        required=False,
        update_allowed=True,
    )
    public_key_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    signature_algorithm_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    signature_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    not_before_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    not_after_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    certificate_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    certificate_signing_request_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    text_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    fingerprint_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    expiry_status_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SSL_CERTIFICATE_EXPIRED', 'SSL_CERTIFICATE_GOOD', 'SSL_CERTIFICATE_EXPIRY_WARNING']),
        ],
    )
    chain_verified_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'version',
        'serial_number',
        'self_signed',
        'issuer',
        'subject',
        'key_params',
        'public_key',
        'signature_algorithm',
        'signature',
        'not_before',
        'not_after',
        'certificate',
        'certificate_signing_request',
        'text',
        'fingerprint',
        'expiry_status',
        'chain_verified',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'version': version_schema,
        'serial_number': serial_number_schema,
        'self_signed': self_signed_schema,
        'issuer': issuer_schema,
        'subject': subject_schema,
        'key_params': key_params_schema,
        'public_key': public_key_schema,
        'signature_algorithm': signature_algorithm_schema,
        'signature': signature_schema,
        'not_before': not_before_schema,
        'not_after': not_after_schema,
        'certificate': certificate_schema,
        'certificate_signing_request': certificate_signing_request_schema,
        'text': text_schema,
        'fingerprint': fingerprint_schema,
        'expiry_status': expiry_status_schema,
        'chain_verified': chain_verified_schema,
    }




class PKIProfile(AviResource):
    resource_name = "pkiprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the PKI Profile"),
        required=True,
        update_allowed=True,
    )
    ca_certs_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SSLCertificate.properties_schema,
        required=True,
        update_allowed=False,
    )
    ca_certs_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of Certificate Authorities (Root and Intermediate) trusted that is used for certificate validation"),
        schema=ca_certs_item_schema,
        required=False,
        update_allowed=True,
    )
    crls_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CRL.properties_schema,
        required=True,
        update_allowed=False,
    )
    crls_schema = properties.Schema(
        properties.Schema.LIST,
        _("Certificate Revocation Lists"),
        schema=crls_item_schema,
        required=False,
        update_allowed=True,
    )
    ignore_peer_chain_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When enabled, Avi will not trust Intermediate and Root certs presented by a client.  Instead, only the chain certs configured in the Certificate Authority section will be used to verify trust of the client's cert."),
        required=False,
        update_allowed=True,
    )
    crl_check_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When enabled, Avi will verify via CRL checks that certificates in the trust chain have not been revoked."),
        required=False,
        update_allowed=True,
    )
    validate_only_leaf_crl_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When enabled, Avi will only validate the revocation status of the leaf certificate using CRL. To enable validation for the entire chain, disable this option and provide all the relevant CRLs"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'ca_certs',
        'crls',
        'ignore_peer_chain',
        'crl_check',
        'validate_only_leaf_crl',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'ca_certs': ca_certs_schema,
        'crls': crls_schema,
        'ignore_peer_chain': ignore_peer_chain_schema,
        'crl_check': crl_check_schema,
        'validate_only_leaf_crl': validate_only_leaf_crl_schema,
    }




class PKIProfileCaCerts(AviNestedResource, SSLCertificate):
    resource_name = "pkiprofile"
    nested_property_name = "ca_certs"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pkiprofile"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = SSLCertificate.PROPERTIES + ('pkiprofile_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'pkiprofile_uuid': parent_uuid_schema,
    }
    properties_schema.update(SSLCertificate.properties_schema)


class PKIProfileCrls(AviNestedResource, CRL):
    resource_name = "pkiprofile"
    nested_property_name = "crls"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pkiprofile"),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = CRL.PROPERTIES + ('pkiprofile_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'pkiprofile_uuid': parent_uuid_schema,
    }
    properties_schema.update(CRL.properties_schema)


def resource_mapping():
    return {
        'Avi::CertificateManagementProfile::ScriptParam': CertificateManagementProfileScriptParams,
        'Avi::SSLProfile::CipherEnum': SSLProfileCipherEnums,
        'Avi::PKIProfile::Crl': PKIProfileCrls,
        'Avi::SSLProfile::Tag': SSLProfileTags,
        'Avi::CertificateManagementProfile': CertificateManagementProfile,
        'Avi::SSLProfile': SSLProfile,
        'Avi::PKIProfile': PKIProfile,
        'Avi::PKIProfile::CaCert': PKIProfileCaCerts,
        'Avi::SSLProfile::AcceptedVersion': SSLProfileAcceptedVersions,
    }

