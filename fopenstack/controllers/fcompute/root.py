from pecan import expose, redirect
from pecan.rest import RestController
from webob.exc import status_map
import logging

import v2

logger = logging.getLogger(__name__)


class RootController(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "versions": [
                {
                    "status": "CURRENT",
                    "updated": "2011-01-21T11:33:21Z",
                    "id": "v2.0",
                    "links": [
                        {
                            "href": "http://23.253.228.211:8774/v2/",
                            "rel": "self"
                        }
                    ]
                },
                {
                    "status": "EXPERIMENTAL",
                    "updated": "2013-07-23T11:33:21Z",
                    "id": "v3.0",
                    "links": [
                        {
                            "href": "http://23.253.228.211:8774/v3/",
                            "rel": "self"
                        }
                    ]
                }
            ]
        }

    v2 = v2.V2Controller()
