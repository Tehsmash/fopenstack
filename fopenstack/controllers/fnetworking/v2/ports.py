from pecan import expose, redirect, abort
from pecan.rest import RestController


PORTS = {
    "ports": [
        {
            "status": "ACTIVE",
            "binding:host_id": "devstack",
            "name": "",
            "allowed_address_pairs": [],
            "admin_state_up": True,
            "network_id": "70c1db1f-b701-45bd-96e0-a313ee3430b3",
            "tenant_id": "",
            "extra_dhcp_opts": [],
            "binding:vif_details": {
                "port_filter": True,
                "ovs_hybrid_plug": True
            },
            "binding:vif_type": "ovs",
            "device_owner": "network:router_gateway",
            "mac_address": "fa:16:3e:58:42:ed",
            "binding:profile": {},
            "binding:vnic_type": "normal",
            "fixed_ips": [
                {
                    "subnet_id": "008ba151-0b8c-4a67-98b5-0d2b87666062",
                    "ip_address": "172.24.4.2"
                }
            ],
            "id": "d80b1a3b-4fc1-49f3-952e-1e2ab7081d8b",
            "security_groups": [],
            "device_id": "9ae135f4-b6e0-4dad-9e91-3c223e385824"
        },
        {
            "status": "ACTIVE",
            "binding:host_id": "devstack",
            "name": "",
            "allowed_address_pairs": [],
            "admin_state_up": True,
            "network_id": "f27aa545-cbdd-4907-b0c6-c9e8b039dcc2",
            "tenant_id": "d397de8a63f341818f198abb0966f6f3",
            "extra_dhcp_opts": [],
            "binding:vif_details": {
                "port_filter": True,
                "ovs_hybrid_plug": True
            },
            "binding:vif_type": "ovs",
            "device_owner": "network:router_interface",
            "mac_address": "fa:16:3e:bb:3c:e4",
            "binding:profile": {},
            "binding:vnic_type": "normal",
            "fixed_ips": [
                {
                    "subnet_id": "288bf4a1-51ba-43b6-9d0a-520e9005db17",
                    "ip_address": "10.0.0.1"
                }
            ],
            "id": "f71a6703-d6de-4be1-a91a-a570ede1d159",
            "security_groups": [],
            "device_id": "9ae135f4-b6e0-4dad-9e91-3c223e385824"
        }
    ]
} 

class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return PORTS

    @expose('json', content_type='application/json')
    def get_one(self, port_id):
        for port in PORTS['ports']:
            if port['id'] == port_id:
                return { 'port': port }
        abort(404)
