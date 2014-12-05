from pecan import expose, redirect
from pecan.rest import RestController

class TenantsController(RestController):
    
    @expose('json', content_type='application/json')
    def get(self):
        return {
            "tenants": [
                {
                    "id": "1234",
                    "name": "ACME Corp",
                    "description": "A description ...",
                    "enabled": True
                },
                {
                    "id": "3456",
                    "name": "Iron Works",
                    "description": "A description ...",
                    "enabled": True
                }
            ],
            "tenants_links": []
        }
