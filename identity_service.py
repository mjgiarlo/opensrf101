from osrf.app import Application
import arkpy


class Identity(Application):

    Application.register_method(
        api_name='psu.stewardship.identity.mint',
        method='mint',
        argc=0,
        stream=False
        )
    def mint(self, request):
        ark = arkpy.mint(authority='42409', template='eeddeeddk')
        request.respond(ark)

    Application.register_method(
        api_name='psu.stewardship.identity.validate',
        method='validate',
        argc=1,
        stream=True
        )
    def validate(self, request, ark=''):
        is_valid = arkpy.validate(ark)
        request.respond(is_valid)


Application.register_app(Identity())
