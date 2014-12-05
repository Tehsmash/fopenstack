from pecan import expose, redirect, abort
from pecan.rest import RestController

import members

IMAGES = {
    "images": [
        {
            "uri": "http://glance.example.com/images/71c675ab-d94f-49cd-a114-e12490b328d9",
            "name": "Ubuntu 10.04 Plain 5GB",
            "disk_format": "vhd",
            "container_format": "ovf",
            "size": "5368709120",
            "checksum": "c2e5db72bd7fd153f53ede5da5a06de3",
            "created_at": "2010-02-03 09:34:01",
            "updated_at": "2010-02-03 09:34:01",
            "deleted_at": "",
            "status": "active",
            "is_public": True,
            "min_ram": 256,
            "min_disk": 5,
            "id": "71c675ab-d94f-49cd-a114-e12490b328d9",
            "owner": None,
            "properties": {
                "distro": "Ubuntu 10.04 LTS"
            }
        }
    ]
} 

class Controller(RestController):

    _custom_actions = {
        'detail': ['GET']
    }

    @expose('json', content_type='application/json')
    def get(self):
        return IMAGES

    @expose('json', content_type='application/json')
    def detail(self):
        return IMAGES

    @expose('json', content_type='application/json')
    def get_one(self, image_id):
        for image in IMAGES['images']:
            if image['id'] == image_id:
                return image
        abort(404)

    members = members.Controller()
