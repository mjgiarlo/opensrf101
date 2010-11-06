import bottle
import hashlib

@bottle.get('/fixity')
def fixity():
    file_location = bottle.request.GET.get('file')
    algo = bottle.request.GET.get('algorithm')
    h = hashlib.new(algo)
    h.update(open(file_location).read())
    checksum = h.hexdigest()
    return "fixity %s generated for %s" % (checksum, file_location)


bottle.run(host='localhost', port='8080')

    


