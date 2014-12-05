from pecan import expose, redirect
from pecan.rest import RestController


class Controller(RestController):

    @expose('json', content_type='application/json')
    def get_one(self, owner_id):
        return {
            "shared_images": [
                {
                    "image_id": "71c675ab-d94f-49cd-a114-e12490b328d9",
                    "can_share": False
                }
            ]
        } 
