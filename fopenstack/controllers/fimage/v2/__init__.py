from pecan import expose, redirect
from pecan.rest import RestController

import images
import schemas

class Controller(RestController):
    images = images.Controller()
    schemas = schemas.Controller()
