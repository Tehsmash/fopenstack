from pecan import expose, redirect, abort
from pecan.rest import RestController

class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return {
            "tenant_usages": [
                {
                    "start": "2012-10-08T21:10:44.587336",
                    "stop": "2012-10-08T22:10:44.587336",
                    "tenant_id": "openstack",
                    "total_hours": 1.0,
                    "total_local_gb_usage": 1.0,
                    "total_memory_mb_usage": 512.0,
                    "total_vcpus_usage": 1.0
                }
            ]
        } 

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id):
        return {
            "tenant_usage": {
                "server_usages": [
                    {
                        "ended_at": None,
                        "flavor": "m1.tiny",
                        "hours": 1.0,
                        "instance_id": "1f1deceb-17b5-4c04-84c7-e0d4499c8fe0",
                        "local_gb": 1,
                        "memory_mb": 512,
                        "name": "new-server-test",
                        "started_at": "2012-10-08T20:10:44.541277",
                        "state": "active",
                        "tenant_id": "openstack",
                        "uptime": 3600,
                        "vcpus": 1
                    }
                ],
                "start": "2012-10-08T20:10:44.587336",
                "stop": "2012-10-08T21:10:44.587336",
                "tenant_id": "openstack",
                "total_hours": 1.0,
                "total_local_gb_usage": 1.0,
                "total_memory_mb_usage": 512.0,
                "total_vcpus_usage": 1.0
            }
        }
