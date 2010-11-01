from osrf.app import Application


class Test(Application):

    Application.register_method(
        api_name='opensrf.test.reverse',
        method='reverse',
        argc=1,
        stream=True
        )
    def reverse(self, request, message=''):
        request.respond(message[::-1])


Application.register_app(Test())
