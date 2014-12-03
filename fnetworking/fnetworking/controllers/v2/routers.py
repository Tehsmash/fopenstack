from pecan import expose, redirect, abort
from pecan.rest import RestController


ROUTERS = {
    "routers": [
        {
            "status": "ACTIVE",
            "external_gateway_info": None,
            "name": "second_routers",
            "admin_state_up": True,
            "tenant_id": "6b96ff0cb17a4b859e1e575d221683d3",
            "id": "7177abc4-5ae9-4bb7-b0d4-89e94a4abf3b"
        },
        {
            "status": "ACTIVE",
            "external_gateway_info": {
                "network_id": "3c5bcddd-6af9-4e6b-9c3e-c153e521cab8"
            },
            "name": "router1",
            "admin_state_up": True,
            "tenant_id": "33a40233088643acb66ff6eb0ebea679",
            "id": "a9254bdb-2613-4a13-ac4c-adc581fba50d"
        }
    ]
}


class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return ROUTERS

    @expose('json', content_type='application/json')
    def get_one(self, router_id):
        for router in ROUTERS['routers']:
            if router['id'] == router_id:
                return { 'router': router }
        abort(404)
