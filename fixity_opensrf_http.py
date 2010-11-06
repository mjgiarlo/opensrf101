import bottle
import osrf.ses
import osrf.system

conf_file = "/opensrf/etc/opensrf_core.xml"


@bottle.get('/fixity')
def fixity():
    f = bottle.request.GET.get('file')
    algo = bottle.request.GET.get('algorithm')
    osrf.system.System.connect(config_file=conf_file,
                               config_context="config.opensrf")
    session = osrf.ses.ClientSession("psu.stewardship.fixity")
    request = session.request("psu.stewardship.fixity.generate", f, algo)
    response = request.recv()
    request.cleanup()
    checksum = response.content()
    session.cleanup()
    return "fixity %s generated for %s" % (checksum, f)


bottle.run(host='localhost', port='8080')
