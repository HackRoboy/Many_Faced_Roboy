import urllib.parse, urllib.request
import codecs
import pickle

def b64pickle(obj):
    return codecs.encode(pickle.dumps(obj), "base64").decode()

def b64unpickle(pickled):
    return pickle.loads(codecs.decode(pickled, "base64"))

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
        if retval == "None":
            return None
        return b64unpickle(retval)
    
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