from osrf.app import Application
from dflat import dflat


class Versioning(Application):

    Application.register_method(
        api_name='psu.stewardship.versioning.init',
        method='init',
        argc=1,
        stream=False
        )
    def init(self, request, obj_dir):
        dflat.init(obj_dir)
        request.respond(dflat.status(obj_dir))
        

Application.register_app(Versioning())
