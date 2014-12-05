from pecan import expose, redirect, abort
from pecan.rest import RestController
from webob.exc import status_map

import v2

class RootController(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return{
            "versions": [
                {
                    "status": "CURRENT",
                    "id": "v2.0",
                    "links": [
                        {
                            "href": "http://localhost:9696/v2.0",
                            "rel": "self"
                        }
                    ]
                }
            ]
        } 

    @expose()
    def _lookup(self, version, *remainder):
        if version == "v2.0": 
            return v2.Controller(), remainder
        else:
            abort(404)
