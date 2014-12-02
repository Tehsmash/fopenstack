from pecan import expose, redirect
from pecan.rest import RestController
from webob.exc import status_map

import v2

class RootController(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "versions":{
                "values":[
                    {
                        "id":"v3.0",
                        "links":[
                            {
                                "href":"http://localhost:5000/v3/",
                                "rel":"self"
                            }
                        ],
                        "media-types":[
                            {
                                "base":"application/json",
                                "type":"application/vnd.openstack.identity-v3+json"
                            },
                            {
                                "base":"application/xml",
                                "type":"application/vnd.openstack.identity-v3+xml"
                            }
                        ],
                        "status":"stable",
                        "updated":"2013-03-06T00:00:00Z"
                    },
                    {
                        "id":"v2.0",
                        "links":[
                            {
                                "href":"http://localhost:5000/v2.0/",
                                "rel":"self"
                            },
                            {
                                "href":"http://docs.openstack.org/",
                                "rel":"describedby",
                                "type":"text/html"
                            }
                        ],
                        "media-types":[
                            {
                                "base":"application/json",
                                "type":"application/vnd.openstack.identity-v2.0+json"
                            },
                            {
                                "base":"application/xml",
                                "type":"application/vnd.openstack.identity-v2.0+xml"
                            }
                        ],
                        "status":"stable",
                        "updated":"2014-04-17T00:00:00Z"
                    }
                ]
            }
        }

    @expose()
    def _lookup(self, version, *remainder):
        if version == "v2.0": 
            return v2.V2Controller(), remainder
        else:
            abort(404)

class AdminRootController(RootController):
    # Do something to signify that its the admin endpoint 
    pass 
