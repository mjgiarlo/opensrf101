import sys
import bagit
import osrf.ses
import osrf.system

conf_file = "/opensrf/etc/opensrf_core.xml"
osrf.system.System.connect(config_file=conf_file,
                           config_context="config.opensrf")

datastore = "/mnt/datastore"

# take a file
d = "/home/mjg/Documents/bagme"
f = "/home/mjg/Documents/bagme/architecture_scratchpad.txt"

# generate an identifier
session = osrf.ses.ClientSession("psu.stewardship.identity")
request = session.request("psu.stewardship.identity.mint")
response = request.recv()
request.cleanup()
ark = response.content()
session.cleanup()
print "identifier %s minted for %s" % (ark, f)

# grab its fixity value
session = osrf.ses.ClientSession("psu.stewardship.fixity")
request = session.request("psu.stewardship.fixity.generate", f, "md5")
response = request.recv()
request.cleanup()
checksum = response.content()
session.cleanup()
print "fixity %s generated for %s" % (checksum, f)

# bag it up
bag = bagit.make_bag(d)
print "bag created at %s" % bag.path
if not bag.validate():
    print "bag not valid"
    sys.exit(1)
        
# stuff in a pairtree
session = osrf.ses.ClientSession("psu.stewardship.storage")
request = session.request("psu.stewardship.storage.store", datastore, ark, bag.path)
response = request.recv()
request.cleanup()
storage_location = response.content()
session.cleanup()
print "bag stored in %s" % storage_location

# create a version
session = osrf.ses.ClientSession("psu.stewardship.versioning")
request = session.request("psu.stewardship.versioning.init", storage_location)
response = request.recv()
request.cleanup()
version = response.content()
session.cleanup()
print "version %s of content created" % version

# check fixity?
# update version?
