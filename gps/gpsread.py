import serial
import json
import urllib.parse, urllib.request
import time, threading
import RPi.GPIO as GPIO
from cacher import mcache
from time import sleep

GPIO.setmode(GPIO.BOARD)
gpio_light = 16
gpio_button = 18
GPIO.setup(gpio_light, GPIO.OUT)
GPIO.setup(gpio_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

gps_data = {}

def checksum(bs):
    num = 0
    for b in bs:
        num = num ^ b
    return num
#print(int("47", 16))
#print(checksum(b"GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,"))

def process_line(line):
    if not line.startswith(b"$"):
        return None
    
    if b"*" in line:
        checkbytes = line[1:line.find(b"*")]
        csum = checksum(checkbytes)
        rcsum = int(line[line.find(b"*")+1:],16)
        if csum != rcsum:
            return None
        line = line[0:line.find(b"*")]
    
    data = line.decode("ascii").split(",")
    return data

print(process_line(b"$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"))
print(process_line(b"GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*43"))
print(process_line(b"$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,"))
print(process_line(b"$GPGSA,A,3,04,05,,09,12,,,24,,,,,2.5,1.3,2.1*39"))
print(process_line(b"$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"))
print(process_line(b"$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6B"))


last_store = time.time()

def store_data():
    global last_store
    tnow = time.time()
    elapsed = tnow - last_store
    
    if elapsed < 3:
        return
    
    mcache.gps = gps_data
    last_store = tnow
    
    print("Transmitted Data!!!")
    
    with open('data.txt', 'w') as outfile:
        json.dump(gps_data, outfile)

def read_serial():
    with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
        while True:
            try:
                line = ser.readline()   # read a '\n' terminated line
                #print(line)

                data = process_line(line)
                if data is None:
                    continue

                gps_data[data[0]] = data[1:]
                store_data()
            except:
                continue
            
            #print(gps_data)

lighton = False

def turn_on_light():
    global lighton
    if lighton:
        return
    lighton = True
    GPIO.output(gpio_light, GPIO.HIGH)
    mcache.light = True

def turn_off_light():
    global lighton
    if not lighton:
        return
    lighton = False
    GPIO.output(gpio_light, GPIO.LOW)
    mcache.light = False

def is_button_pressed():
    return not GPIO.input(gpio_button)

def is_in_range(quest):
    try:
        lat = float(gps_data["$GPGGA"][1])
        lon = float(gps_data["$GPGGA"][3])
        
        if abs(lat - quest["lat"]) > quest["radius"]:
            return False
        
        if abs(lon - quest["lon"]) > quest["radius"]:
            return False
        
        return True
    except:
        return False #DEBUG CHANGE LATER

cur_quest = None
cur_autoinrange = False
lid = 0
def check_quest():
    global cur_quest, cur_autoinrange, lid
    while True:
        cur_quest = mcache.gpsquest
        cur_autoinrange = mcache.autoinrange
        if cur_quest["id"] < 0:
            lid = 0
        if cur_quest is None or cur_quest["id"] < lid:
            turn_off_light()
            continue
        print(is_in_range(cur_quest), is_button_pressed())
        
        if is_in_range(cur_quest) or cur_autoinrange:
            turn_on_light()
        else:
            turn_off_light()

def check_button():
    global lid
    while True:
        if is_button_pressed():
            print(is_in_range(cur_quest), True)
            if cur_quest is None or cur_quest["id"] < 0:
                continue
            if is_in_range(cur_quest) or cur_autoinrange:
                lid = cur_quest["id"] + 1
                turn_off_light()
                mcache.queststate = True
        sleep(0.1)

def main():
    t = threading.Thread(target=read_serial)
    t.start()
    t2 = threading.Thread(target=check_quest)
    t2.start()
    t3 = threading.Thread(target=check_button)
    t3.start()

if __name__ == '__main__':
    main()


"""
GGA          Global Positioning System Fix Data
123519       Fix taken at 12:35:19 UTC
4807.038,N   Latitude 48 deg 07.038' N
01131.000,E  Longitude 11 deg 31.000' E
1            Fix quality: 0 = invalid
                        1 = GPS fix (SPS)
                        2 = DGPS fix
                        3 = PPS fix
            4 = Real Time Kinematic
            5 = Float RTK
                        6 = estimated (dead reckoning) (2.3 feature)
            7 = Manual input mode
            8 = Simulation mode
08           Number of satellites being tracked
0.9          Horizontal dilution of position
545.4,M      Altitude, Meters, above mean sea level
46.9,M       Height of geoid (mean sea level) above WGS84
                ellipsoid
(empty field) time in seconds since last DGPS update
(empty field) DGPS station ID number
*47          the checksum data, always begins with *
"""