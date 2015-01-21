from pecan import expose, redirect, abort
from pecan.rest import RestController


QUOTAS = {
    "quota": {
        "subnet": 10,
        "router": 10,
        "port": 50,
        "network": 10,
        "floatingip": 50
    }
}  


class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self):
        return QUOTAS

    @expose('json', content_type='application/json')
    def get_one(self, quota_id):
        for quota in QUOTAS['quotas']:
            if quota['id'] == quota_id:
                return { 'quota': quota }
        abort(404)
