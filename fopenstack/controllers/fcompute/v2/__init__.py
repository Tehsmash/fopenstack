from pecan import expose, redirect, abort
from pecan.rest import RestController

import limits
import extensions
import servers
import flavors
import images

class V2Controller(RestController):

    limits = limits.Controller()
    extensions = extensions.Controller()
    servers = servers.Controller()
    flavors = flavors.Controller()
    images = images.Controller()

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "version": {
                "status": "CURRENT",
                "updated": "2011-01-21T11:33:21Z",
                "media-types": [
                    {
                        "base": "application/xml",
                        "type": "application/vnd.openstack.compute+xml;version=2"
                    },
                    {
                        "base": "application/json",
                        "type": "application/vnd.openstack.compute+json;version=2"
                    }
                ],
                "id": "v2.0",
                "links": [
                    {
                        "href": "http://23.253.228.211:8774/v2/",
                        "rel": "self"
                    },
                    {
                        "href": "http://docs.openstack.org/api/openstack-compute/2/os-compute-devguide-2.pdf",
                        "type": "application/pdf",
                        "rel": "describedby"
                    },
                    {
                        "href": "http://docs.openstack.org/api/openstack-compute/2/wadl/os-compute-2.wadl",
                        "type": "application/vnd.sun.wadl+xml",
                        "rel": "describedby"
                    }
                ]
            }
        }

    @expose('json', content_type='application/json')
    def get_one(self, project_id):
        abort(404)

    @expose('json', content_type='application/json')
    def _lookup(self, project_id, name, *remainder):
        for extension in extensions.EXTENSION_CONTROLLERS:
            if extension == name:
                return extensions.EXTENSION_CONTROLLERS[extension](), remainder
        abort(404)
