import os
from osrf.app import Application
import osrf.log
import pairtree


class Storage(Application):

    Application.register_method(
        api_name='psu.stewardship.storage.store',
        method='store',
        argc=3,
        stream=False
        )
    def store(self, request, base_location, identifier, source):
        f = pairtree.PairtreeStorageFactory()
        tree_location = os.path.join(base_location, "stewardship")
        pairstore = f.get_store(store_dir=tree_location, uri_base="ark://")
        pairobj = pairstore.create_object(identifier)
        pairobj.add_directory(source)
        request.respond(pairobj.location)


Application.register_app(Storage())
