from pecan import expose, redirect, abort
from pecan.rest import RestController


IPS = {
    "addresses": {
        "public": [
            {
                "version": 4,
                "addr": "67.23.10.132"
            },
            {
                "version": 6,
                "addr": "::babe:67.23.10.132"
            },
            {
                "version": 4,
                "addr": "67.23.10.131"
            },
            {
                "version": 6,
                "addr": "::babe:4317:0A83"
            }
        ],
        "private": [
            {
                "version": 4,
                "addr": "10.176.42.16"
            },
            {
                "version": 6,
                "addr": "::babe:10.176.42.16"
            }
        ]
    }
} 


class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self, tenant_id, server_id):
        return IPS

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id, server_id, network_name):
        data = IPS['addresses'].get(network_name, None)
        if data is None:
            abort(404)
        else:
            return {'network': {'id': network_name, 'ip': data}}
