from pecan import expose, redirect, abort
from pecan.rest import RestController

import tags
import members

IMAGES = {
    "images": [
        {
            "status": "active",
            "name": "cirros-0.3.2-x86_64-disk",
            "tags": [],
            "container_format": "bare",
            "created_at": "2014-11-07T17:07:06Z",
            "disk_format": "qcow2",
            "updated_at": "2014-11-07T17:19:09Z",
            "visibility": "public",
            "self": "/v2/images/1bea47ed-f6a9-463b-b423-14b9cca9ad27",
            "min_disk": 0,
            "protected": False,
            "id": "1bea47ed-f6a9-463b-b423-14b9cca9ad27",
            "file": "/v2/images/1bea47ed-f6a9-463b-b423-14b9cca9ad27/file",
            "checksum": "64d7c1cd2b6f60c92c14662941cb7913",
            "owner": "5ef70662f8b34079a6eddb8da9d75fe8",
            "size": 13167616,
            "min_ram": 0,
            "schema": "/v2/schemas/image"
        },
        {
            "status": "active",
            "name": "F17-x86_64-cfntools",
            "tags": [],
            "container_format": "bare",
            "created_at": "2014-10-30T08:23:39Z",
            "disk_format": "qcow2",
            "updated_at": "2014-11-03T16:40:10Z",
            "visibility": "public",
            "self": "/v2/images/781b3762-9469-4cec-b58d-3349e5de4e9c",
            "min_disk": 0,
            "protected": False,
            "id": "781b3762-9469-4cec-b58d-3349e5de4e9c",
            "file": "/v2/images/781b3762-9469-4cec-b58d-3349e5de4e9c/file",
            "checksum": "afab0f79bac770d61d24b4d0560b5f70",
            "owner": "5ef70662f8b34079a6eddb8da9d75fe8",
            "size": 476704768,
            "min_ram": 0,
            "schema": "/v2/schemas/image"
        }
    ],
    "schema": "/v2/schemas/images",
    "first": "/v2/images"
}

class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return IMAGES

    @expose('json', content_type='application/json')
    def get_one(self, image_id):
        for image in IMAGES['images']:
            if image['id'] == image_id:
                return image
        abort(404)

    tags = tags.Controller()
    members = members.Controller()
