from pecan import expose, redirect, request
from pecan.rest import RestController

EXTENSIONS = {
    "extensions": {
        "values": [
            {
                "updated": "2013-07-07T12:00:0-00:00",
                "name": "OpenStack S3 API",
                "links": [
                    {
                        "href": "https://github.com/openstack/identity-api",
                        "type": "text/html",
                        "rel": "describedby"
                    }
                ],
                "namespace": "http://docs.openstack.org/identity/api/ext/s3tokens/v1.0",
                "alias": "s3tokens",
                "description": "OpenStack S3 API."
            },
            {
                "updated": "2013-07-23T12:00:0-00:00",
                "name": "OpenStack Keystone Endpoint Filter API",
                "links": [
                    {
                        "href": "https://github.com/openstack/identity-api/blob/master/openstack-identity-api/v3/src/markdown/identity-api-v3-os-ep-filter-ext.md",
                        "type": "text/html",
                        "rel": "describedby"
                    }
                ],
                "namespace": "http://docs.openstack.org/identity/api/ext/OS-EP-FILTER/v1.0",
                "alias": "OS-EP-FILTER",
                "description": "OpenStack Keystone Endpoint Filter API."
            },
            {
                "updated": "2013-12-17T12:00:0-00:00",
                "name": "OpenStack Federation APIs",
                "links": [
                    {
                        "href": "https://github.com/openstack/identity-api",
                        "type": "text/html",
                        "rel": "describedby"
                    }
                ],
                "namespace": "http://docs.openstack.org/identity/api/ext/OS-FEDERATION/v1.0",
                "alias": "OS-FEDERATION",
                "description": "OpenStack Identity Providers Mechanism."
            },
            {
                "updated": "2013-07-11T17:14:00-00:00",
                "name": "OpenStack Keystone Admin",
                "links": [
                    {
                        "href": "https://github.com/openstack/identity-api",
                        "type": "text/html",
                        "rel": "describedby"
                    }
                ],
                "namespace": "http://docs.openstack.org/identity/api/ext/OS-KSADM/v1.0",
                "alias": "OS-KSADM",
                "description": "OpenStack extensions to Keystone v2.0 API enabling Administrative Operations."
            },
            {
                "updated": "2014-01-20T12:00:0-00:00",
                "name": "OpenStack Simple Certificate API",
                "links": [
                    {
                        "href": "https://github.com/openstack/identity-api",
                        "type": "text/html",
                        "rel": "describedby"
                    }
                ],
                "namespace": "http://docs.openstack.org/identity/api/ext/OS-SIMPLE-CERT/v1.0",
                "alias": "OS-SIMPLE-CERT",
                "description": "OpenStack simple certificate retrieval extension"
            },
            {
                "updated": "2013-07-07T12:00:0-00:00",
                "name": "OpenStack EC2 API",
                "links": [
                    {
                        "href": "https://github.com/openstack/identity-api",
                        "type": "text/html",
                        "rel": "describedby"
                    }
                ],
                "namespace": "http://docs.openstack.org/identity/api/ext/OS-EC2/v1.0",
                "alias": "OS-EC2",
                "description": "OpenStack EC2 Credentials backend."
            }
        ]
    }
}

class ExtensionsController(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return EXTENSIONS

    @expose('json', content_type='application/json')
    def get_one(self, id):
        for extension in EXTENSIONS['extensions']['values']:
            if extension['alias'] == id:
                return { 'extension': extension }
        abort(404)
