from pecan import expose, redirect, abort
from pecan.rest import RestController

EXTENSIONS = {
    "extensions": [
        {
            "alias": "NMN",
            "description": "Multiple network support.",
            "links": [],
            "name": "Multinic",
            "namespace": "http://docs.openstack.org/compute/ext/multinic/api/v1.1",
            "updated": "2011-06-09T00:00:00+00:00"
        },
        {
            "alias": "OS-DCF",
            "description": "Disk Management Extension.",
            "links": [],
            "name": "DiskConfig",
            "namespace": "http://docs.openstack.org/compute/ext/disk_config/api/v1.1",
            "updated": "2011-09-27T00:00:00+00:00"
        },
        {
            "alias": "OS-EXT-AZ",
            "description": "Extended Server Attributes support.",
            "links": [],
            "name": "ExtendedAvailabilityZone",
            "namespace": "http://docs.openstack.org/compute/ext/extended_availability_zone/api/v2",
            "updated": "2013-01-30T00:00:00+00:00"
        },
        {
            "alias": "OS-EXT-IMG-SIZE",
            "description": "Adds image size to image listings.",
            "links": [],
            "name": "ImageSize",
            "namespace": "http://docs.openstack.org/compute/ext/image_size/api/v1.1",
            "updated": "2013-02-19T00:00:00+00:00"
        },
        {
            "alias": "OS-EXT-IPS",
            "description": "Adds type parameter to the ip list.",
            "links": [],
            "name": "ExtendedIps",
            "namespace": "http://docs.openstack.org/compute/ext/extended_ips/api/v1.1",
            "updated": "2013-01-06T00:00:00+00:00"
        },
        {
            "alias": "OS-EXT-IPS-MAC",
            "description": "Adds mac address parameter to the ip list.",
            "links": [],
            "name": "ExtendedIpsMac",
            "namespace": "http://docs.openstack.org/compute/ext/extended_ips_mac/api/v1.1",
            "updated": "2013-03-07T00:00:00+00:00"
        },
        {
            "alias": "OS-EXT-SRV-ATTR",
            "description": "Extended Server Attributes support.",
            "links": [],
            "name": "ExtendedServerAttributes",
            "namespace": "http://docs.openstack.org/compute/ext/extended_status/api/v1.1",
            "updated": "2011-11-03T00:00:00+00:00"
        },
        {
            "alias": "OS-EXT-STS",
            "description": "Extended Status support.",
            "links": [],
            "name": "ExtendedStatus",
            "namespace": "http://docs.openstack.org/compute/ext/extended_status/api/v1.1",
            "updated": "2011-11-03T00:00:00+00:00"
        },
        {
            "alias": "OS-EXT-VIF-NET",
            "description": "Adds network id parameter to the virtual interface list.",
            "links": [],
            "name": "ExtendedVIFNet",
            "namespace": "http://docs.openstack.org/compute/ext/extended-virtual-interfaces-net/api/v1.1",
            "updated": "2013-03-07T00:00:00+00:00"
        },
        {
            "alias": "OS-FLV-DISABLED",
            "description": "Support to show the disabled status of a flavor.",
            "links": [],
            "name": "FlavorDisabled",
            "namespace": "http://docs.openstack.org/compute/ext/flavor_disabled/api/v1.1",
            "updated": "2012-08-29T00:00:00+00:00"
        },
        {
            "alias": "OS-FLV-EXT-DATA",
            "description": "Provide additional data for flavors.",
            "links": [],
            "name": "FlavorExtraData",
            "namespace": "http://docs.openstack.org/compute/ext/flavor_extra_data/api/v1.1",
            "updated": "2011-09-14T00:00:00+00:00"
        },
        {
            "alias": "OS-SCH-HNT",
            "description": "Pass arbitrary key/value pairs to the scheduler.",
            "links": [],
            "name": "SchedulerHints",
            "namespace": "http://docs.openstack.org/compute/ext/scheduler-hints/api/v2",
            "updated": "2011-07-19T00:00:00+00:00"
        },
        {
            "alias": "OS-SRV-USG",
            "description": "Adds launched_at and terminated_at on Servers.",
            "links": [],
            "name": "ServerUsage",
            "namespace": "http://docs.openstack.org/compute/ext/server_usage/api/v1.1",
            "updated": "2013-04-29T00:00:00+00:00"
        },
        {
            "alias": "os-admin-actions",
            "description": "Enable admin-only server actions\n\n    Actions include: pause, unpause, suspend, resume, migrate,\n    resetNetwork, injectNetworkInfo, lock, unlock, createBackup\n    ",
            "links": [],
            "name": "AdminActions",
            "namespace": "http://docs.openstack.org/compute/ext/admin-actions/api/v1.1",
            "updated": "2011-09-20T00:00:00+00:00"
        },
        {
            "alias": "os-agents",
            "description": "Agents support.",
            "links": [],
            "name": "Agents",
            "namespace": "http://docs.openstack.org/compute/ext/agents/api/v2",
            "updated": "2012-10-28T00:00:00-00:00"
        },
        {
            "alias": "os-aggregates",
            "description": "Admin-only aggregate administration.",
            "links": [],
            "name": "Aggregates",
            "namespace": "http://docs.openstack.org/compute/ext/aggregates/api/v1.1",
            "updated": "2012-01-12T00:00:00+00:00"
        },
        {
            "alias": "os-assisted-volume-snapshots",
            "description": "Assisted volume snapshots.",
            "links": [],
            "name": "AssistedVolumeSnapshots",
            "namespace": "http://docs.openstack.org/compute/ext/assisted-volume-snapshots/api/v2",
            "updated": "2013-08-29T00:00:00-00:00"
        },
        {
            "alias": "os-attach-interfaces",
            "description": "Attach interface support.",
            "links": [],
            "name": "AttachInterfaces",
            "namespace": "http://docs.openstack.org/compute/ext/interfaces/api/v1.1",
            "updated": "2012-07-22T00:00:00+00:00"
        },
        {
            "alias": "os-availability-zone",
            "description": "1. Add availability_zone to the Create Server v1.1 API.\n       2. Add availability zones describing.\n    ",
            "links": [],
            "name": "AvailabilityZone",
            "namespace": "http://docs.openstack.org/compute/ext/availabilityzone/api/v1.1",
            "updated": "2012-12-21T00:00:00+00:00"
        },
        {
            "alias": "os-baremetal-ext-status",
            "description": "Add extended status in Baremetal Nodes v2 API.",
            "links": [],
            "name": "BareMetalExtStatus",
            "namespace": "http://docs.openstack.org/compute/ext/baremetal_ext_status/api/v2",
            "updated": "2013-08-27T00:00:00+00:00"
        },
        {
            "alias": "os-baremetal-nodes",
            "description": "Admin-only bare-metal node administration.",
            "links": [],
            "name": "BareMetalNodes",
            "namespace": "http://docs.openstack.org/compute/ext/baremetal_nodes/api/v2",
            "updated": "2013-01-04T00:00:00+00:00"
        },
        {
            "alias": "os-block-device-mapping-v2-boot",
            "description": "Allow boot with the new BDM data format.",
            "links": [],
            "name": "BlockDeviceMappingV2Boot",
            "namespace": "http://docs.openstack.org/compute/ext/block_device_mapping_v2_boot/api/v2",
            "updated": "2013-07-08T00:00:00+00:00"
        },
        {
            "alias": "os-cell-capacities",
            "description": "Adding functionality to get cell capacities.",
            "links": [],
            "name": "CellCapacities",
            "namespace": "http://docs.openstack.org/compute/ext/cell_capacities/api/v1.1",
            "updated": "2013-05-27T00:00:00+00:00"
        },
        {
            "alias": "os-cells",
            "description": "Enables cells-related functionality such as adding neighbor cells,\n    listing neighbor cells, and getting the capabilities of the local cell.\n    ",
            "links": [],
            "name": "Cells",
            "namespace": "http://docs.openstack.org/compute/ext/cells/api/v1.1",
            "updated": "2013-05-14T00:00:00+00:00"
        },
        {
            "alias": "os-certificates",
            "description": "Certificates support.",
            "links": [],
            "name": "Certificates",
            "namespace": "http://docs.openstack.org/compute/ext/certificates/api/v1.1",
            "updated": "2012-01-19T00:00:00+00:00"
        },
        {
            "alias": "os-cloudpipe",
            "description": "Adds actions to create cloudpipe instances.\n\n    When running with the Vlan network mode, you need a mechanism to route\n    from the public Internet to your vlans.  This mechanism is known as a\n    cloudpipe.\n\n    At the time of creating this class, only OpenVPN is supported.  Support for\n    a SSH Bastion host is forthcoming.\n    ",
            "links": [],
            "name": "Cloudpipe",
            "namespace": "http://docs.openstack.org/compute/ext/cloudpipe/api/v1.1",
            "updated": "2011-12-16T00:00:00+00:00"
        },
        {
            "alias": "os-cloudpipe-update",
            "description": "Adds the ability to set the vpn ip/port for cloudpipe instances.",
            "links": [],
            "name": "CloudpipeUpdate",
            "namespace": "http://docs.openstack.org/compute/ext/cloudpipe-update/api/v2",
            "updated": "2012-11-14T00:00:00+00:00"
        },
        {
            "alias": "os-config-drive",
            "description": "Config Drive Extension.",
            "links": [],
            "name": "ConfigDrive",
            "namespace": "http://docs.openstack.org/compute/ext/config_drive/api/v1.1",
            "updated": "2012-07-16T00:00:00+00:00"
        },
        {
            "alias": "os-console-output",
            "description": "Console log output support, with tailing ability.",
            "links": [],
            "name": "ConsoleOutput",
            "namespace": "http://docs.openstack.org/compute/ext/os-console-output/api/v2",
            "updated": "2011-12-08T00:00:00+00:00"
        },
        {
            "alias": "os-consoles",
            "description": "Interactive Console support.",
            "links": [],
            "name": "Consoles",
            "namespace": "http://docs.openstack.org/compute/ext/os-consoles/api/v2",
            "updated": "2011-12-23T00:00:00+00:00"
        },
        {
            "alias": "os-create-server-ext",
            "description": "Extended support to the Create Server v1.1 API.",
            "links": [],
            "name": "Createserverext",
            "namespace": "http://docs.openstack.org/compute/ext/createserverext/api/v1.1",
            "updated": "2011-07-19T00:00:00+00:00"
        },
        {
            "alias": "os-deferred-delete",
            "description": "Instance deferred delete.",
            "links": [],
            "name": "DeferredDelete",
            "namespace": "http://docs.openstack.org/compute/ext/deferred-delete/api/v1.1",
            "updated": "2011-09-01T00:00:00+00:00"
        },
        {
            "alias": "os-evacuate",
            "description": "Enables server evacuation.",
            "links": [],
            "name": "Evacuate",
            "namespace": "http://docs.openstack.org/compute/ext/evacuate/api/v2",
            "updated": "2013-01-06T00:00:00+00:00"
        },
        {
            "alias": "os-extended-floating-ips",
            "description": "Adds optional fixed_address to the add floating IP command.",
            "links": [],
            "name": "ExtendedFloatingIps",
            "namespace": "http://docs.openstack.org/compute/ext/extended_floating_ips/api/v2",
            "updated": "2013-04-19T00:00:00+00:00"
        },
        {
            "alias": "os-extended-quotas",
            "description": "Adds ability for admins to delete quota\n    and optionally force the update Quota command.\n    ",
            "links": [],
            "name": "ExtendedQuotas",
            "namespace": "http://docs.openstack.org/compute/ext/extended_quotas/api/v1.1",
            "updated": "2013-06-09T00:00:00+00:00"
        },
        {
            "alias": "os-extended-hypervisors",
            "description": "Extended hypervisors support.",
            "links": [],
            "name": "ExtendedHypervisors",
            "namespace": "http://docs.openstack.org/compute/ext/extended_hypervisors/api/v1.1",
            "updated": "2013-10-21T00:00:00-00:00"
        },
        {
            "alias": "os-extended-services",
            "description": "Extended services support.",
            "links": [],
            "name": "ExtendedServices",
            "namespace": "http://docs.openstack.org/compute/ext/extended_services/api/v2",
            "updated": "2013-05-17T00:00:00-00:00"
        },
        {
            "alias": "os-extended-volumes",
            "description": "Extended Volumes support.",
            "links": [],
            "name": "ExtendedVolumes",
            "namespace": "http://docs.openstack.org/compute/ext/extended_volumes/api/v1.1",
            "updated": "2013-06-07T00:00:00+00:00"
        },
        {
            "alias": "os-fixed-ips",
            "description": "Fixed IPs support.",
            "links": [],
            "name": "FixedIPs",
            "namespace": "http://docs.openstack.org/compute/ext/fixed_ips/api/v2",
            "updated": "2012-10-18T13:25:27-06:00"
        },
        {
            "alias": "os-flavor-access",
            "description": "Flavor access support.",
            "links": [],
            "name": "FlavorAccess",
            "namespace": "http://docs.openstack.org/compute/ext/flavor_access/api/v2",
            "updated": "2012-08-01T00:00:00+00:00"
        },
        {
            "alias": "os-flavor-extra-specs",
            "description": "Instance type (flavor) extra specs.",
            "links": [],
            "name": "FlavorExtraSpecs",
            "namespace": "http://docs.openstack.org/compute/ext/flavor_extra_specs/api/v1.1",
            "updated": "2011-06-23T00:00:00+00:00"
        },
        {
            "alias": "os-flavor-manage",
            "description": "\n    Flavor create/delete API support\n    ",
            "links": [],
            "name": "FlavorManage",
            "namespace": "http://docs.openstack.org/compute/ext/flavor_manage/api/v1.1",
            "updated": "2012-01-19T00:00:00+00:00"
        },
        {
            "alias": "os-flavor-rxtx",
            "description": "Support to show the rxtx status of a flavor.",
            "links": [],
            "name": "FlavorRxtx",
            "namespace": "http://docs.openstack.org/compute/ext/flavor_rxtx/api/v1.1",
            "updated": "2012-08-29T00:00:00+00:00"
        },
        {
            "alias": "os-flavor-swap",
            "description": "Support to show the swap status of a flavor.",
            "links": [],
            "name": "FlavorSwap",
            "namespace": "http://docs.openstack.org/compute/ext/flavor_swap/api/v1.1",
            "updated": "2012-08-29T00:00:00+00:00"
        },
        {
            "alias": "os-floating-ip-dns",
            "description": "Floating IP DNS support.",
            "links": [],
            "name": "FloatingIpDns",
            "namespace": "http://docs.openstack.org/ext/floating_ip_dns/api/v1.1",
            "updated": "2011-12-23T00:00:00+00:00"
        },
        {
            "alias": "os-floating-ip-pools",
            "description": "Floating IPs support.",
            "links": [],
            "name": "FloatingIpPools",
            "namespace": "http://docs.openstack.org/compute/ext/floating_ip_pools/api/v1.1",
            "updated": "2012-01-04T00:00:00+00:00"
        },
        {
            "alias": "os-floating-ips",
            "description": "Floating IPs support.",
            "links": [],
            "name": "FloatingIps",
            "namespace": "http://docs.openstack.org/compute/ext/floating_ips/api/v1.1",
            "updated": "2011-06-16T00:00:00+00:00"
        },
        {
            "alias": "os-floating-ips-bulk",
            "description": "Bulk handling of Floating IPs.",
            "links": [],
            "name": "FloatingIpsBulk",
            "namespace": "http://docs.openstack.org/compute/ext/floating_ips_bulk/api/v2",
            "updated": "2012-10-29T13:25:27-06:00"
        },
        {
            "alias": "os-fping",
            "description": "Fping Management Extension.",
            "links": [],
            "name": "Fping",
            "namespace": "http://docs.openstack.org/compute/ext/fping/api/v1.1",
            "updated": "2012-07-06T00:00:00+00:00"
        },
        {
            "alias": "os-hide-server-addresses",
            "description": "Support hiding server addresses in certain states.",
            "links": [],
            "name": "HideServerAddresses",
            "namespace": "http://docs.openstack.org/compute/ext/hide_server_addresses/api/v1.1",
            "updated": "2012-12-11T00:00:00+00:00"
        },
        {
            "alias": "os-hosts",
            "description": "Admin-only host administration.",
            "links": [],
            "name": "Hosts",
            "namespace": "http://docs.openstack.org/compute/ext/hosts/api/v1.1",
            "updated": "2011-06-29T00:00:00+00:00"
        },
        {
            "alias": "os-hypervisors",
            "description": "Admin-only hypervisor administration.",
            "links": [],
            "name": "Hypervisors",
            "namespace": "http://docs.openstack.org/compute/ext/hypervisors/api/v1.1",
            "updated": "2012-06-21T00:00:00+00:00"
        },
        {
            "alias": "os-instance-actions",
            "description": "View a log of actions and events taken on an instance.",
            "links": [],
            "name": "InstanceActions",
            "namespace": "http://docs.openstack.org/compute/ext/instance-actions/api/v1.1",
            "updated": "2013-02-08T00:00:00+00:00"
        },
        {
            "alias": "os-server-external-events",
            "description": "Server External Event Triggers.",
            "links": [],
            "name": "ServerExternalEvents",
            "namespace": "http://docs.openstack.org/compute/ext/server-external-events/api/v2",
            "updated": "2014-02-18T00:00:00-00:00"
        },
        {
            "alias": "os-server-groups",
            "description": "Server group support.",
            "links": [],
            "name": "ServerGroups",
            "namespace": "http://docs.openstack.org/compute/ext/servergroups/api/v2",
            "updated": "2013-06-01T00:00:00+00:00"
        },
        {
            "alias": "os-instance_usage_audit_log",
            "description": "Admin-only Task Log Monitoring.",
            "links": [],
            "name": "OSInstanceUsageAuditLog",
            "namespace": "http://docs.openstack.org/ext/services/api/v1.1",
            "updated": "2012-07-06T01:00:00+00:00"
        },
        {
            "alias": "os-keypairs",
            "description": "Keypair Support.",
            "links": [],
            "name": "Keypairs",
            "namespace": "http://docs.openstack.org/compute/ext/keypairs/api/v1.1",
            "updated": "2011-08-08T00:00:00+00:00"
        },
        {
            "alias": "os-migrations",
            "description": "Provide data on migrations.",
            "links": [],
            "name": "Migrations",
            "namespace": "http://docs.openstack.org/compute/ext/migrations/api/v2.0",
            "updated": "2013-05-30T00:00:00+00:00"
        },
        {
            "alias": "os-multiple-create",
            "description": "Allow multiple create in the Create Server v1.1 API.",
            "links": [],
            "name": "MultipleCreate",
            "namespace": "http://docs.openstack.org/compute/ext/multiplecreate/api/v1.1",
            "updated": "2012-08-07T00:00:00+00:00"
        },
        {
            "alias": "os-networks",
            "description": "Admin-only Network Management Extension.",
            "links": [],
            "name": "Networks",
            "namespace": "http://docs.openstack.org/compute/ext/os-networks/api/v1.1",
            "updated": "2011-12-23T00:00:00+00:00"
        },
        {
            "alias": "os-networks-associate",
            "description": "Network association support.",
            "links": [],
            "name": "NetworkAssociationSupport",
            "namespace": "http://docs.openstack.org/compute/ext/networks_associate/api/v2",
            "updated": "2012-11-19T00:00:00+00:00"
        },
        {
            "alias": "os-preserve-ephemeral-rebuild",
            "description": "Allow preservation of the ephemeral partition on rebuild.",
            "links": [],
            "name": "PreserveEphemeralOnRebuild",
            "namespace": "http://docs.openstack.org/compute/ext/preserve_ephemeral_rebuild/api/v2",
            "updated": "2013-12-17T00:00:00+00:00"
        },
        {
            "alias": "os-quota-sets",
            "description": "Quotas management support.",
            "links": [],
            "name": "Quotas",
            "namespace": "http://docs.openstack.org/compute/ext/quotas-sets/api/v1.1",
            "updated": "2011-08-08T00:00:00+00:00"
        },
        {
            "alias": "os-rescue",
            "description": "Instance rescue mode.",
            "links": [],
            "name": "Rescue",
            "namespace": "http://docs.openstack.org/compute/ext/rescue/api/v1.1",
            "updated": "2011-08-18T00:00:00+00:00"
        },
        {
            "alias": "os-extended-rescue-with-image",
            "description": "Rescue instance with the image specified.",
            "links": [],
            "name": "ExtendedRescueWithImage",
            "namespace": "http://docs.openstack.org/compute/ext/extended_rescue_with_image/api/v2",
            "updated": "2014-03-05T00:00:00+00:00"
        },
        {
            "alias": "os-security-group-default-rules",
            "description": "Default rules for security group support.",
            "links": [],
            "name": "SecurityGroupDefaultRules",
            "namespace": "http://docs.openstack.org/compute/ext/securitygroupdefaultrules/api/v1.1",
            "updated": "2013-02-05T00:00:00+00:00"
        },
        {
            "alias": "os-security-groups",
            "description": "Security group support.",
            "links": [],
            "name": "SecurityGroups",
            "namespace": "http://docs.openstack.org/compute/ext/securitygroups/api/v1.1",
            "updated": "2013-05-28T00:00:00+00:00"
        },
        {
            "alias": "os-server-diagnostics",
            "description": "Allow Admins to view server diagnostics through server action.",
            "links": [],
            "name": "ServerDiagnostics",
            "namespace": "http://docs.openstack.org/compute/ext/server-diagnostics/api/v1.1",
            "updated": "2011-12-21T00:00:00+00:00"
        },
        {
            "alias": "os-server-password",
            "description": "Server password support.",
            "links": [],
            "name": "ServerPassword",
            "namespace": "http://docs.openstack.org/compute/ext/server-password/api/v2",
            "updated": "2012-11-29T00:00:00+00:00"
        },
        {
            "alias": "os-server-start-stop",
            "description": "Start/Stop instance compute API support.",
            "links": [],
            "name": "ServerStartStop",
            "namespace": "http://docs.openstack.org/compute/ext/servers/api/v1.1",
            "updated": "2012-01-23T00:00:00+00:00"
        },
        {
            "alias": "os-services",
            "description": "Services support.",
            "links": [],
            "name": "Services",
            "namespace": "http://docs.openstack.org/compute/ext/services/api/v2",
            "updated": "2012-10-28T00:00:00-00:00"
        },
        {
            "alias": "os-shelve",
            "description": "Instance shelve mode.",
            "links": [],
            "name": "Shelve",
            "namespace": "http://docs.openstack.org/compute/ext/shelve/api/v1.1",
            "updated": "2013-04-06T00:00:00+00:00"
        },
        {
            "alias": "os-simple-tenant-usage",
            "description": "Simple tenant usage extension.",
            "links": [],
            "name": "SimpleTenantUsage",
            "namespace": "http://docs.openstack.org/compute/ext/os-simple-tenant-usage/api/v1.1",
            "updated": "2011-08-19T00:00:00+00:00"
        },
        {
            "alias": "os-tenant-networks",
            "description": "Tenant-based Network Management Extension.",
            "links": [],
            "name": "OSTenantNetworks",
            "namespace": "http://docs.openstack.org/compute/ext/os-tenant-networks/api/v2",
            "updated": "2012-03-07T09:46:43-05:00"
        },
        {
            "alias": "os-used-limits",
            "description": "Provide data on limited resources that are being used.",
            "links": [],
            "name": "UsedLimits",
            "namespace": "http://docs.openstack.org/compute/ext/used_limits/api/v1.1",
            "updated": "2012-07-13T00:00:00+00:00"
        },
        {
            "alias": "os-used-limits-for-admin",
            "description": "Provide data to admin on limited resources used by other tenants.",
            "links": [],
            "name": "UsedLimitsForAdmin",
            "namespace": "http://docs.openstack.org/compute/ext/used_limits_for_admin/api/v1.1",
            "updated": "2013-05-02T00:00:00+00:00"
        },
        {
            "alias": "os-user-data",
            "description": "Add user_data to the Create Server v1.1 API.",
            "links": [],
            "name": "UserData",
            "namespace": "http://docs.openstack.org/compute/ext/userdata/api/v1.1",
            "updated": "2012-08-07T00:00:00+00:00"
        },
        {
            "alias": "os-user-quotas",
            "description": "Project user quota support.",
            "links": [],
            "name": "UserQuotas",
            "namespace": "http://docs.openstack.org/compute/ext/user_quotas/api/v1.1",
            "updated": "2013-07-18T00:00:00+00:00"
        },
        {
            "alias": "os-virtual-interfaces",
            "description": "Virtual interface support.",
            "links": [],
            "name": "VirtualInterfaces",
            "namespace": "http://docs.openstack.org/compute/ext/virtual_interfaces/api/v1.1",
            "updated": "2011-08-17T00:00:00+00:00"
        },
        {
            "alias": "os-volume-attachment-update",
            "description": "Support for updating a volume attachment.",
            "links": [],
            "name": "VolumeAttachmentUpdate",
            "namespace": "http://docs.openstack.org/compute/ext/os-volume-attachment-update/api/v2",
            "updated": "2013-06-20T00:00:00-00:00"
        },
        {
            "alias": "os-volumes",
            "description": "Volumes support.",
            "links": [],
            "name": "Volumes",
            "namespace": "http://docs.openstack.org/compute/ext/volumes/api/v1.1",
            "updated": "2011-03-25T00:00:00+00:00"
        },
        {
            "alias": "os-extended-services-delete",
            "description": "Services deletion support.",
            "links": [],
            "name": "ExtendedServicesDelete",
            "namespace": "http://docs.openstack.org/compute/ext/extended_services_delete/api/v2",
            "updated": "2013-12-10T00:00:00+00:00"
        },
        {
            "alias": "os-console-auth-tokens",
            "description": "Console token authentication support.",
            "links": [],
            "name": "ConsoleAuthTokens",
            "namespace": "http://docs.openstack.org/compute/ext/consoles-auth-tokens/api/v2",
            "updated": "2013-08-13T00:00:00+00:00"
        }
    ]
}

import simple_tenant_usage
import floating_ips

EXTENSION_CONTROLLERS = {
        'os-simple-tenant-usage': simple_tenant_usage.Controller,
        'os-floating-ips': floating_ips.Controller
}

class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self, tenant_id):
        return EXTENSIONS

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id, alias):
        for extension in EXTENSIONS['extensions']:
            if extension['alias'] == alias:
                return { 'extension': extension }
        abort(404)
