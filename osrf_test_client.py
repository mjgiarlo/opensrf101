import sys
import osrf.ses
import osrf.system

conf_file = "/opensrf/etc/opensrf_core.xml"

osrf.system.System.connect(config_file=conf_file,
                           config_context="config.opensrf")

reversed = osrf.ses.ClientSession.atomic_request("opensrf.test",
                                                 "opensrf.test.reverse",
                                                 sys.argv[1])
print reversed


