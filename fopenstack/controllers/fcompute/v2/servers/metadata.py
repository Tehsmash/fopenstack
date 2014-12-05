from pecan import expose, redirect, abort
from pecan.rest import RestController


METADATA = {
    "metadata": {
        "foo": "Foo Value"
    }
}



class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self, tenant_id, server_id):
        return METADATA

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id, server_id, key):
        data = METADATA['metadata'].get(key, None)
        if data is None:
            abort(404)
        else:
            return { "metadata": { key: data } }
