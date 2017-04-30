from cacher import mcache
import threading
from time import sleep
import math

last_id = -1
cur_quest = {"id":-1, "lat":0, "lon":0, "radius":0}
gps_state = None
cur_callback = None

def convertdec(coor):
    dec, integ = math.modf(coor)
    return integ * 100 + dec * 60

def set_quest(lat, lon, callback = None, radius = 0.01):
    global cur_quest, cur_callback, last_id
    last_id += 1
    cur_quest = {"id":last_id, "lon":lon, "lat":lat, "radius":radius}
    cur_callback = callback

def worker():
    global cur_quest, gps_state
    focus = False
    while True:
        mcache.gpsquest = cur_quest
        gps_state = mcache.gps
        quest_state = mcache.queststate
        
        if quest_state is True:
            if cur_callback is not None:
                cur_callback()
            cur_quest = {"id":-1, "lat":0, "lon":0, "radius":0}
            mcache.gpsquest = cur_quest
            mcache.queststate = False

def main():
    t = threading.Thread(target=worker)
    t.start()

if __name__ == '__main__':
    main()