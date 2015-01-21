from pecan import expose, redirect, abort
from pecan.rest import RestController

class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "floating_ips": [
                {
                    "fixed_ip": None,
                    "id": 1,
                    "instance_id": None,
                    "ip": "10.10.10.1",
                    "pool": "nova"
                },
                {
                    "fixed_ip": None,
                    "id": 2,
                    "instance_id": None,
                    "ip": "10.10.10.2",
                    "pool": "nova"
                }
            ]
        } 

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id):
        return {
            "floating_ip": {
                "fixed_ip": None,
                "id": 1,
                "instance_id": None,
                "ip": "10.10.10.1",
                "pool": "nova"
            }
        }
