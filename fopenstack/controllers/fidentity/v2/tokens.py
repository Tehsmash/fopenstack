from pecan import expose, redirect
from pecan.rest import RestController

import datetime

dt = datetime.datetime.now()
dtlater = datetime.datetime(datetime.MAXYEAR, 1, 1) 

class TokensController(RestController):

    @expose('json', content_type='application/json')
    def post(self):
        return {
            "access": {
                "token": {
                    "issued_at": dt.isoformat(),
                    "expires": dtlater.isoformat(),
                    "id": "aaaaa-bbbbb-ccccc-dddd",
                    "tenant": {
                        "description": None,
                        "enabled": True,
                        "id": "fc394f2ab2df4114bde39905f800dc57",
                        "name": "demo"
                    }
                },
                "serviceCatalog": [
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:8774/v2/fc394f2ab2df4114bde39905f800dc57",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:8774/v2/fc394f2ab2df4114bde39905f800dc57",
                                "id": "2dad48f09e2a447a9bf852bcd93548ef",
                                "publicURL": "http://localhost:8774/v2/fc394f2ab2df4114bde39905f800dc57"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "compute",
                        "name": "nova"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:9696/",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:9696/",
                                "id": "97c526db8d7a4c88bbb8d68db1bdcdb8",
                                "publicURL": "http://localhost:9696/"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "network",
                        "name": "neutron"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:8776/v2/fc394f2ab2df4114bde39905f800dc57",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:8776/v2/fc394f2ab2df4114bde39905f800dc57",
                                "id": "93f86dfcbba143a39a33d0c2cd424870",
                                "publicURL": "http://localhost:8776/v2/fc394f2ab2df4114bde39905f800dc57"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "volumev2",
                        "name": "cinder"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:8774/v3",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:8774/v3",
                                "id": "3eb274b12b1d47b2abc536038d87339e",
                                "publicURL": "http://localhost:8774/v3"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "computev3",
                        "name": "nova"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:3333",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:3333",
                                "id": "957f1e54afc64d33a62099faa5e980a2",
                                "publicURL": "http://localhost:3333"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "s3",
                        "name": "s3"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:9292",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:9292",
                                "id": "27d5749f36864c7d96bebf84a5ec9767",
                                "publicURL": "http://localhost:9292"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "image",
                        "name": "glance"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:8776/v1/fc394f2ab2df4114bde39905f800dc57",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:8776/v1/fc394f2ab2df4114bde39905f800dc57",
                                "id": "37c83a2157f944f1972e74658aa0b139",
                                "publicURL": "http://localhost:8776/v1/fc394f2ab2df4114bde39905f800dc57"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "volume",
                        "name": "cinder"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:8773/services/Admin",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:8773/services/Cloud",
                                "id": "289b59289d6048e2912b327e5d3240ca",
                                "publicURL": "http://localhost:8773/services/Cloud"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "ec2",
                        "name": "ec2"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:8080",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:8080/v1/AUTH_fc394f2ab2df4114bde39905f800dc57",
                                "id": "16b76b5e5b7d48039a6e4cc3129545f3",
                                "publicURL": "http://localhost:8080/v1/AUTH_fc394f2ab2df4114bde39905f800dc57"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "object-store",
                        "name": "swift"
                    },
                    {
                        "endpoints": [
                            {
                                "adminURL": "http://localhost:35357/v2.0",
                                "region": "RegionOne",
                                "internalURL": "http://localhost:5000/v2.0",
                                "id": "26af053673df4ef3a2340c4239e21ea2",
                                "publicURL": "http://localhost:5000/v2.0"
                            }
                        ],
                        "endpoints_links": [],
                        "type": "identity",
                        "name": "keystone"
                    }
                ],
                "user": {
                    "username": "demo",
                    "roles_links": [],
                    "id": "9a6590b2ab024747bc2167c4e064d00d",
                    "roles": [
                        {
                            "name": "Member"
                        },
                        {
                            "name": "anotherrole"
                        }
                    ],
                    "name": "demo"
                },
                "metadata": {
                    "is_admin": 1,
                    "roles": [
                        "7598ac3c634d4c3da4b9126a5f67ca2b",
                        "f95c0ab82d6045d9805033ee1fbc80d4"
                    ]
                }
            }
        }

