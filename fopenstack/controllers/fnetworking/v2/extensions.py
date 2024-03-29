from pecan import expose, redirect, abort
from pecan.rest import RestController


EXTENSIONS = {
    "extensions": [
        {
            "updated": "2013-01-20T00:00:00-00:00",
            "name": "Neutron Service Type Management",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/neutron/service-type/api/v1.0",
            "alias": "service-type",
            "description": "API for retrieving service providers for Neutron advanced services"
        },
        {
            "updated": "2012-10-05T10:00:00-00:00",
            "name": "security-group",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/securitygroups/api/v2.0",
            "alias": "security-group",
            "description": "The security groups extension."
        },
        {
            "updated": "2013-02-07T10:00:00-00:00",
            "name": "L3 Agent Scheduler",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/l3_agent_scheduler/api/v1.0",
            "alias": "l3_agent_scheduler",
            "description": "Schedule routers among l3 agents"
        },
        {
            "updated": "2013-02-07T10:00:00-00:00",
            "name": "Loadbalancer Agent Scheduler",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/lbaas_agent_scheduler/api/v1.0",
            "alias": "lbaas_agent_scheduler",
            "description": "Schedule pools among lbaas agents"
        },
        {
            "updated": "2013-03-28T10:00:00-00:00",
            "name": "Neutron L3 Configurable external gateway mode",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/neutron/ext-gw-mode/api/v1.0",
            "alias": "ext-gw-mode",
            "description": "Extension of the router abstraction for specifying whether SNAT should occur on the external gateway"
        },
        {
            "updated": "2014-02-03T10:00:00-00:00",
            "name": "Port Binding",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/binding/api/v1.0",
            "alias": "binding",
            "description": "Expose port bindings of a virtual port to external application"
        },
        {
            "updated": "2012-09-07T10:00:00-00:00",
            "name": "Provider Network",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/provider/api/v1.0",
            "alias": "provider",
            "description": "Expose mapping of virtual networks to physical networks"
        },
        {
            "updated": "2013-02-03T10:00:00-00:00",
            "name": "agent",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/agent/api/v2.0",
            "alias": "agent",
            "description": "The agent management extension."
        },
        {
            "updated": "2012-07-29T10:00:00-00:00",
            "name": "Quota management support",
            "links": [],
            "namespace": "http://docs.openstack.org/network/ext/quotas-sets/api/v2.0",
            "alias": "quotas",
            "description": "Expose functions for quotas management per tenant"
        },
        {
            "updated": "2013-02-07T10:00:00-00:00",
            "name": "DHCP Agent Scheduler",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/dhcp_agent_scheduler/api/v1.0",
            "alias": "dhcp_agent_scheduler",
            "description": "Schedule networks among dhcp agents"
        },
        {
            "updated": "2013-06-27T10:00:00-00:00",
            "name": "Multi Provider Network",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/multi-provider/api/v1.0",
            "alias": "multi-provider",
            "description": "Expose mapping of virtual networks to multiple physical networks"
        },
        {
            "updated": "2013-01-14T10:00:00-00:00",
            "name": "Neutron external network",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/neutron/external_net/api/v1.0",
            "alias": "external-net",
            "description": "Adds external network attribute to network resource."
        },
        {
            "updated": "2012-07-20T10:00:00-00:00",
            "name": "Neutron L3 Router",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/neutron/router/api/v1.0",
            "alias": "router",
            "description": "Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway."
        },
        {
            "updated": "2013-07-23T10:00:00-00:00",
            "name": "Allowed Address Pairs",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/allowedaddresspairs/api/v2.0",
            "alias": "allowed-address-pairs",
            "description": "Provides allowed address pairs"
        },
        {
            "updated": "2013-03-17T12:00:00-00:00",
            "name": "Neutron Extra DHCP opts",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/neutron/extra_dhcp_opt/api/v1.0",
            "alias": "extra_dhcp_opt",
            "description": "Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)"
        },
        {
            "updated": "2012-10-07T10:00:00-00:00",
            "name": "LoadBalancing service",
            "links": [],
            "namespace": "http://wiki.openstack.org/neutron/LBaaS/API_1.0",
            "alias": "lbaas",
            "description": "Extension for LoadBalancing service"
        },
        {
            "updated": "2013-02-01T10:00:00-00:00",
            "name": "Neutron Extra Route",
            "links": [],
            "namespace": "http://docs.openstack.org/ext/neutron/extraroutes/api/v1.0",
            "alias": "extraroute",
            "description": "Extra routes configuration for L3 router"
        }
    ]
} 

class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return EXTENSIONS

    @expose('json', content_type='application/json')
    def get_one(self, alias):
        for extension in EXTENSIONS['extensions']:
            if extension['alias'] == alias:
                return { 'extension': extension } 
        abort(404)
