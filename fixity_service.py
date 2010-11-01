import hashlib
from osrf.app import Application


class Fixity(Application):

    Application.register_method(
        api_name='psu.stewardship.fixity.generate',
        method='generate',
        argc=2,
        stream=False
        )
    def generate(self, request, file_location, algorithm):
        h = hashlib.new(algorithm)
        h.update(open(file_location).read())
        request.respond(h.hexdigest())


Application.register_app(Fixity())
