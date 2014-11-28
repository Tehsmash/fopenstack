from pecan import expose, redirect, request
from pecan.rest import RestController

import tenants
import tokens

class V2Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "version": {
                "status": "stable",
                "updated": "2013-03-06T00:00:00Z",
                "media-types": [
                    {
                        "base": "application/json",
                        "type": "application/vnd.openstack.identity-v3+json"
                    },
                    {
                        "base": "application/xml",
                        "type": "application/vnd.openstack.identity-v3+xml"
                    }
                ],
                "id": "v3.0",
                "links": [
                    {
                        "href": "http://23.253.228.211:35357/v3/",
                        "rel": "self"
                    }
                ]
            }
        }

    @expose()
    def _lookup(self, endpoint, *remainder):
        if endpoint == "extensions": 
            return V2ExtensionsController(), remainder
        elif endpoint == "tokens":
            return tokens.TokensController(), remainder
        elif endpoint == "tenants":
            return tenants.TenantsController(), remainder
        else:
            abort(404)
