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
ark = osrf.ses.ClientSession.atomic_request("psu.stewardship.identity",
                                            "psu.stewardship.identity.mint")
print "identifier %s minted for %s" % (ark, f)

# grab its fixity value
checksum = osrf.ses.ClientSession.atomic_request("psu.stewardship.fixity",
                                                 "psu.stewardship.fixity.generate",
                                                 f,
                                                 "md5")
print "fixity %s generated for %s" % (checksum, f)

# bag it up
bag = bagit.make_bag(d)
print "bag created at %s" % bag.path
if not bag.validate():
    print "bag not valid"
    sys.exit(1)
        
# stuff in a pairtree
storage_location = osrf.ses.ClientSession.atomic_request("psu.stewardship.storage",
                                                         "psu.stewardship.storage.store",
                                                         datastore,
                                                         ark,
                                                         bag.path)
print "bag stored in %s" % storage_location

# create a version
version = osrf.ses.ClientSession.atomic_request("psu.stewardship.versioning",
                                                "psu.stewardship.versioning.init",
                                                storage_location)
print "version %s of content created" % version

# check fixity?
# update version?
