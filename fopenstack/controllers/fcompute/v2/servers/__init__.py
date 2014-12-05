from pecan import expose, redirect, abort
from pecan.rest import RestController

import metadata
import ips

SERVERS = {
    "servers": [
        {
            "accessIPv4": "",
            "accessIPv6": "",
            "addresses": {
                "private": [
                    {
                        "addr": "192.168.0.3",
                        "version": 4
                    }
                ]
            },
            "created": "2012-09-07T16:56:37Z",
            "flavor": {
                "id": "1",
                "links": [
                    {
                        "href": "http://openstack.example.com/openstack/flavors/1",
                        "rel": "bookmark"
                    }
                ]
            },
            "hostId": "16d193736a5cfdb60c697ca27ad071d6126fa13baeb670fc9d10645e",
            "id": "05184ba3-00ba-4fbc-b7a2-03b62b884931",
            "image": {
                "id": "70a599e0-31e7-49b7-b260-868f441e862b",
                "links": [
                    {
                        "href": "http://openstack.example.com/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
                        "rel": "bookmark"
                    }
                ]
            },
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/servers/05184ba3-00ba-4fbc-b7a2-03b62b884931",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/servers/05184ba3-00ba-4fbc-b7a2-03b62b884931",
                    "rel": "bookmark"
                }
            ],
            "metadata": {
                "My Server Name": "Apache1"
            },
            "name": "new-server-test",
            "progress": 0,
            "status": "ACTIVE",
            "tenant_id": "openstack",
            "updated": "2012-09-07T16:56:37Z",
            "user_id": "fake"
        }
    ]
}


class Controller(RestController):

    _custom_actions = {
        'detail': ['GET']
    }

    @expose('json', content_type='application/json')
    def get(self, tenant_id):
        keys = ['id', 'links', 'name']
        result = { 'servers': [] }
        for server in SERVERS['servers']:
            result['servers'].append({ key: server[key] for key in keys }) 
        return result

    @expose('json', content_type='application/json')
    def post(self, tenant_id):
        pass

    @expose('json', content_type='application/json')
    def detail(self, tenant_id):
        return SERVERS

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id, server_id):
        for server in SERVERS['servers']:
            if server['id'] == server_id:
                return { 'server': server }
        abort(404)

    
    @expose('json', content_type='application/json')
    def put(self, tenant_id, server_id):
        pass 

    @expose('json', content_type='application/json')
    def delete(self, tenant_id, server_id):
        pass

    metadata = metadata.Controller()
    ips = ips.Controller()
