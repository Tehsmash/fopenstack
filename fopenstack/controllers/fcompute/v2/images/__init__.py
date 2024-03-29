from pecan import expose, redirect, abort
from pecan.rest import RestController

import metadata

IMAGES = {
    "images": [
        {
            "created": "2011-01-01T01:02:03Z",
            "id": "70a599e0-31e7-49b7-b260-868f441e862b",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "architecture": "x86_64",
                "auto_disk_config": "True",
                "kernel_id": "nokernel",
                "ramdisk_id": "nokernel"
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage7",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        },
        {
            "created": "2011-01-01T01:02:03Z",
            "id": "155d900f-4e14-4e4c-a73d-069cbf4541e6",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/images/155d900f-4e14-4e4c-a73d-069cbf4541e6",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/images/155d900f-4e14-4e4c-a73d-069cbf4541e6",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/openstack/images/155d900f-4e14-4e4c-a73d-069cbf4541e6",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "architecture": "x86_64",
                "kernel_id": "nokernel",
                "ramdisk_id": "nokernel"
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage123456",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        },
        {
            "created": "2011-01-01T01:02:03Z",
            "id": "a2459075-d96c-40d5-893e-577ff92e721c",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/images/a2459075-d96c-40d5-893e-577ff92e721c",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/images/a2459075-d96c-40d5-893e-577ff92e721c",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/openstack/images/a2459075-d96c-40d5-893e-577ff92e721c",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "kernel_id": "nokernel",
                "ramdisk_id": "nokernel"
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage123456",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        },
        {
            "created": "2011-01-01T01:02:03Z",
            "id": "a440c04b-79fa-479c-bed1-0b816eaec379",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/images/a440c04b-79fa-479c-bed1-0b816eaec379",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/images/a440c04b-79fa-479c-bed1-0b816eaec379",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/openstack/images/a440c04b-79fa-479c-bed1-0b816eaec379",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "architecture": "x86_64",
                "auto_disk_config": "False",
                "kernel_id": "nokernel",
                "ramdisk_id": "nokernel"
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage6",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        },
        {
            "created": "2011-01-01T01:02:03Z",
            "id": "c905cedb-7281-47e4-8a62-f26bc5fc4c77",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/images/c905cedb-7281-47e4-8a62-f26bc5fc4c77",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/images/c905cedb-7281-47e4-8a62-f26bc5fc4c77",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/openstack/images/c905cedb-7281-47e4-8a62-f26bc5fc4c77",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "kernel_id": "155d900f-4e14-4e4c-a73d-069cbf4541e6",
                "ramdisk_id": None
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage123456",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        },
        {
            "created": "2011-01-01T01:02:03Z",
            "id": "cedef40a-ed67-4d10-800e-17455edce175",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/images/cedef40a-ed67-4d10-800e-17455edce175",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/images/cedef40a-ed67-4d10-800e-17455edce175",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/openstack/images/cedef40a-ed67-4d10-800e-17455edce175",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "kernel_id": "nokernel",
                "ramdisk_id": "nokernel"
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage123456",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        },
        {
            "created": "2011-01-01T01:02:03Z",
            "id": "76fa36fc-c930-4bf3-8c8a-ea2a2420deb6",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/images/76fa36fc-c930-4bf3-8c8a-ea2a2420deb6",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/images/76fa36fc-c930-4bf3-8c8a-ea2a2420deb6",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/openstack/images/76fa36fc-c930-4bf3-8c8a-ea2a2420deb6",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "kernel_id": "nokernel",
                "ramdisk_id": "nokernel"
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage123456",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        }
    ]
} 


class Controller(RestController):
   
    _custom_actions = {
        'detail': ['GET']
    }

    @expose('json', content_type='application/json')
    def get(self, tenant_id):
        return IMAGES

    @expose('json', content_type='application/json')
    def detail(self, tenant_id):
        return IMAGES

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id, image_id):
        for image in IMAGES['images']:
            if image['id'] == image_id:
                return { "image": image }
        abort(404)

    metadata = metadata.Controller()
