import urllib.parse, urllib.request
import codecs
import pickle
import base64

def b64pickle(obj):
    return base64.b32encode(pickle.dumps(obj))

def b64unpickle(pickled):
    return pickle.loads(base64.b32decode(pickled))

class MagnificentCache:
    geturl = "http://themagnificentcacher.appspot.com/get/{name}"
    seturl = "http://themagnificentcacher.appspot.com/set/{name}/{data}"
    def __init__(self):
        pass
    
    def __getattr__(self, name):
        try:
            retval = urllib.request.urlopen(MagnificentCache.geturl.format(name = name)).read()
        except:
            return None
        if retval == b"None":
            return None
        try:
            return b64unpickle(retval)
        except:
            return None
    
    def __setattr__(self, name, value):
        sval = urllib.parse.quote(b64pickle(value))
        dval = urllib.parse.quote(str(value))
        try:
            retval = urllib.request.urlopen(MagnificentCache.seturl.format(name = name, data=sval)).read()
            retval = urllib.request.urlopen(MagnificentCache.seturl.format(name = "__"+name, data=dval)).read()
        except:
            return

mcache = MagnificentCache()

def main():
    mcache.test = {"hello":"world"}
    print(mcache.test)

if __name__ == '__main__':
    main()