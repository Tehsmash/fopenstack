from pecan import expose, redirect, abort
from pecan.rest import RestController


FLAVORS = {
    "flavors": [
        {
            "id": "1",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/flavors/1",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/flavors/1",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.tiny"
        },
        {
            "id": "2",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/flavors/2",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/flavors/2",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.small"
        },
        {
            "id": "3",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/flavors/3",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/flavors/3",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.medium"
        },
        {
            "id": "4",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/flavors/4",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/flavors/4",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.large"
        },
        {
            "id": "5",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/flavors/5",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/flavors/5",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.xlarge"
        }
    ]
} 


class Controller(RestController):
    
    _custom_actions = {
        'detail': ['GET']
    }

    @expose('json', content_type='application/json')
    def get(self, tenant_id):
        return FLAVORS

    @expose('json', content_type='application/json')
    def detail(self, tenant_id):
        return FLAVORS

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id, flavor_id):
        for flavor in FLAVORS['flavors']:
            if flavor['id'] == flavor_id:
                return { "flavor": flavor }
        abort(404)
