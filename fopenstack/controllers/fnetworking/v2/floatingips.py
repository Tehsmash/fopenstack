from pecan import expose, redirect, abort
from pecan.rest import RestController


class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "floatingips": [
                {
                    "router_id": "d23abc8d-2991-4a55-ba98-2aaea84cc72f",
                    "tenant_id": "4969c491a3c74ee4af974e6d800c62de",
                    "floating_network_id": "376da547-b977-4cfe-9cba-275c80debf57",
                    "fixed_ip_address": "10.0.0.3",
                    "floating_ip_address": "172.24.4.228",
                    "port_id": "f71a6703-d6de-4be1-a91a-a570ede1d159",
                    "id": "2f245a7b-796b-4f26-9cf9-9e82d248fda7"
                },
            ]
        } 

    @expose('json', content_type='application/json')
    def get_one(self, id):
        return {
            "floatingip": {
                "router_id": "d23abc8d-2991-4a55-ba98-2aaea84cc72f",
                "tenant_id": "4969c491a3c74ee4af974e6d800c62de",
                "floating_network_id": "376da547-b977-4cfe-9cba-275c80debf57",
                "fixed_ip_address": "10.0.0.3",
                "floating_ip_address": "172.24.4.228",
                "port_id": "f71a6703-d6de-4be1-a91a-a570ede1d159",
                "id": "2f245a7b-796b-4f26-9cf9-9e82d248fda7"
            }
        } 
