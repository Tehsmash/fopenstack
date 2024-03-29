from pecan import expose, redirect, abort
from pecan.rest import RestController

MEMBERS = {
    "members": [
        {
            "created_at": "2013-10-07T17:58:03Z",
            "image_id": "dbc999e3-c52f-4200-bedd-3b18fe7f87fe",
            "member_id": "123456789",
            "schema": "/v2/schemas/member",
            "status": "pending",
            "updated_at": "2013-10-07T17:58:03Z"
        },
        {
            "created_at": "2013-10-07T17:58:55Z",
            "image_id": "dbc999e3-c52f-4200-bedd-3b18fe7f87fe",
            "member_id": "987654321",
            "schema": "/v2/schemas/member",
            "status": "accepted",
            "updated_at": "2013-10-08T12:08:55Z"
        }
    ],
    "schema": "/v2/schemas/members"
} 


class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self, image_id):
        return MEMBERS

    @expose('json', content_type='application/json')
    def get_one(self, image_id, member_id):
        for member in MEMBERS['members']:
            if member['member_id'] == member_id:
                return member
        abort(404)
