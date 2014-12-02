from pecan import expose, redirect, abort
from pecan.rest import RestController


METADATA = {
    "metadata": {
        "architecture": "x86_64",
        "auto_disk_config": "True",
        "kernel_id": "nokernel",
        "ramdisk_id": "nokernel"
    }
}


class Controller(RestController):

    @expose('json', content_type='application/json')
    def get(self, tenant_id, image_id):
        return METADATA

    @expose('json', content_type='application/json')
    def get_one(self, tenant_id, image_id, key):
        data = METADATA['metadata'].get(key, None)
        if data is None:
            abort(404)
        else:
            return { "metadata": { key: data } }
