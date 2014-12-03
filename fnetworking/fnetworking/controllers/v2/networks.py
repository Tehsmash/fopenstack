from pecan import expose, redirect, abort
from pecan.rest import RestController


NETWORKS ={
    "networks": [
        {
            "status": "ACTIVE",
            "subnets": [
                "54d6f61d-db07-451c-9ab3-b9609b6b6f0b"
            ],
            "name": "private-network",
            "provider:physical_network": None,
            "admin_state_up": True,
            "tenant_id": "4fd44f30292945e481c7b8a0c8908869",
            "provider:network_type": "local",
            "router:external": True,
            "shared": True,
            "id": "d32019d3-bc6e-4319-9c1d-6722fc136a22",
            "provider:segmentation_id": None
        },
        {
            "status": "ACTIVE",
            "subnets": [
                "08eae331-0402-425a-923c-34f7cfe39c1b"
            ],
            "name": "private",
            "provider:physical_network": None,
            "admin_state_up": True,
            "tenant_id": "26a7980765d0414dbc1fc1f88cdb7e6e",
            "provider:network_type": "local",
            "router:external": True,
            "shared": True,
            "id": "db193ab3-96e3-4cb3-8fc5-05f4296d0324",
            "provider:segmentation_id": None
        }
    ]
} 

class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return NETWORKS

    @expose('json', content_type='application/json')
    def get_one(self, network_id):
        for network in NETWORKS['networks']:
            if network['id'] == network_id:
                return { 'network': network }
        abort(404)
