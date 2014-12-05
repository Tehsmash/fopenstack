from pecan import expose, redirect
from pecan.rest import RestController
from webob.exc import status_map

import v2
import v1

class RootController(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "versions": [
                {
                    "status": "CURRENT",
                    "id": "v2.2",
                    "links": [
                        {
                            "href": "http://23.253.228.211:9292/v2/",
                            "rel": "self"
                        }
                    ]
                },
                {
                    "status": "SUPPORTED",
                    "id": "v2.1",
                    "links": [
                        {
                            "href": "http://23.253.228.211:9292/v2/",
                            "rel": "self"
                        }
                    ]
                },
                {
                    "status": "SUPPORTED",
                    "id": "v2.0",
                    "links": [
                        {
                            "href": "http://23.253.228.211:9292/v2/",
                            "rel": "self"
                        }
                    ]
                },
                {
                    "status": "CURRENT",
                    "id": "v1.1",
                    "links": [
                        {
                            "href": "http://23.253.228.211:9292/v1/",
                            "rel": "self"
                        }
                    ]
                },
                {
                    "status": "SUPPORTED",
                    "id": "v1.0",
                    "links": [
                        {
                            "href": "http://23.253.228.211:9292/v1/",
                            "rel": "self"
                        }
                    ]
                }
            ]
        }

    v2 = v2.Controller()
    v1 = v1.Controller()
