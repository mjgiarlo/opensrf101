import sys
import osrf.ses
import osrf.system

conf_file = "/opensrf/etc/opensrf_core.xml"

osrf.system.System.connect(config_file=conf_file,
                           config_context="config.opensrf")

session = osrf.ses.ClientSession("opensrf.test")
request = session.request("opensrf.test.reverse", sys.argv[1])
response = request.recv()
request.cleanup()
print response.content()

session.cleanup()

