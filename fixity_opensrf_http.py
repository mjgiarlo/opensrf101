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
    checksum = osrf.ses.ClientSession.atomic_request("psu.stewardship.fixity",
                                                     "psu.stewardship.fixity.generate",
                                                     f,
                                                     algo)
    return "fixity %s generated for %s" % (checksum, f)


bottle.run(host='localhost', port='8080')
