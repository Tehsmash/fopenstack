from pecan import expose, redirect, abort
from pecan.rest import RestController

import images
import sharedimages

class Controller(RestController):
    @expose()
    def _lookup(self, controller, *remainder):
        if controller == "shared-images":
            return sharedimages.Controller(), remainder
        elif controller == "images":
            return images.Controller(), remainder
        abort(404)
