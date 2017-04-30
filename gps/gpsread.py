import serial
import json
import urllib.parse, urllib.request
import time, threading
import RPi.GPIO as GPIO
from cacher import mcache
from time import sleep

GPIO.setmode(GPIO.BOARD)
gpio_buzzer = 7
gpio_light = 16
gpio_button = 18
GPIO.setup(gpio_light, GPIO.OUT)
GPIO.setup(gpio_buzzer, GPIO.OUT)
pwm_buzzer = GPIO.PWM(gpio_buzzer, 0.5)
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
        if cur_quest is not None and cur_quest["id"] < 0:
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
    while True:
        music()



def tone(freq, duration):
    pwm_buzzer.ChangeFrequency(freq)
    pwm_buzzer.start(0.5)
    time.sleep(duration)
    pwm_buzzer.stop()

def delay(duration):
    time.sleep(duration)

def music():
	C0 = 16.35
	Db0 = 17.32
	D0 = 18.35
	Eb0 = 19.45
	E0 = 20.60
	F0 = 21.83
	Gb0 = 23.12
	G0 = 24.50
	Ab0 = 25.96
	LA0 = 27.50
	Bb0 = 29.14
	B0 = 30.87
	C1 = 32.70
	Db1 = 34.65
	D1 = 36.71
	Eb1 = 38.89
	E1 = 41.20
	F1 = 43.65
	Gb1 = 46.25
	G1 = 49.00
	Ab1 = 51.91
	LA1 = 55.00
	Bb1 = 58.27
	B1 = 61.74
	C2 = 65.41
	Db2 = 69.30
	D2 = 73.42
	Eb2 = 77.78
	E2 = 82.41
	F2 = 87.31
	Gb2 = 92.50
	G2 = 98.00
	Ab2 = 103.83
	LA2 = 110.00
	Bb2 = 116.54
	B2 = 123.47
	C3 = 130.81
	Db3 = 138.59
	D3 = 146.83
	Eb3 = 155.56
	E3 = 164.81
	F3 = 174.61
	Gb3 = 185.00
	G3 = 196.00
	Ab3 = 207.65
	LA3 = 220.00
	Bb3 = 233.08
	B3 = 246.94
	C4 = 261.63
	Db4 = 277.18
	D4 = 293.66
	Eb4 = 311.13
	E4 = 329.63
	F4 = 349.23
	Gb4 = 369.99
	G4 = 392.00
	Ab4 = 415.30
	LA4 = 440.00
	Bb4 = 466.16
	B4 = 493.88
	C5 = 523.25
	Db5 = 554.37
	D5 = 587.33
	Eb5 = 622.25
	E5 = 659.26
	F5 = 698.46
	Gb5 = 739.99
	G5 = 783.99
	Ab5 = 830.61
	LA5 = 880.00
	Bb5 = 932.33
	B5 = 987.77
	C6 = 1046.50
	Db6 = 1108.73
	D6 = 1174.66
	Eb6 = 1244.51
	E6 = 1318.51
	F6 = 1396.91
	Gb6 = 1479.98
	G6 = 1567.98
	Ab6 = 1661.22
	LA6 = 1760.00
	Bb6 = 1864.66
	B6 = 1975.53
	C7 = 2093.00
	Db7 = 2217.46
	D7 = 2349.32
	Eb7 = 2489.02
	E7 = 2637.02
	F7 = 2793.83
	Gb7 = 2959.96
	G7 = 3135.96
	Ab7 = 3322.44
	LA7 = 3520.01
	Bb7 = 3729.31
	B7 = 3951.07
	C8 = 4186.01
	Db8 = 4434.92
	D8 = 4698.64
	Eb8 = 4978.03
	# DURATION OF THE NOTES 
	BPM = 240.0    #  you can change this value changing all the others
	Q = 60/BPM #quarter 1/4 
	H = 2*Q #half 2/4
	E = Q/2   #eighth 1/8
	S = Q/4 # sixteenth 1/16
	W = 4*Q # whole 4/4
	#tone(pin, note, duration)
	tone(LA3,Q); 
	delay(0.001+Q); #delay duration should always be 1 ms more than the note in order to separate them.
	tone(LA3,Q);
	delay(0.001+Q);
	tone(LA3,Q);
	delay(0.001+Q);
	tone(F3,E+S);
	delay(0.001+E+S);
	tone(C4,S);
	delay(0.001+S);

	tone(LA3,Q);
	delay(0.001+Q);
	tone(F3,E+S);
	delay(0.001+E+S);
	tone(C4,S);
	delay(0.001+S);
	tone(LA3,H);
	delay(0.001+H);

	tone(E4,Q); 
	delay(0.001+Q); 
	tone(E4,Q);
	delay(0.001+Q);
	tone(E4,Q);
	delay(0.001+Q);
	tone(F4,E+S);
	delay(0.001+E+S);
	tone(C4,S);
	delay(0.001+S);

	tone(Ab3,Q);
	delay(0.001+Q);
	tone(F3,E+S);
	delay(0.001+E+S);
	tone(C4,S);
	delay(0.001+S);
	tone(LA3,H);
	delay(0.001+H);

	tone(LA4,Q);
	delay(0.001+Q);
	tone(LA3,E+S);
	delay(0.001+E+S);
	tone(LA3,S);
	delay(0.001+S);
	tone(LA4,Q);
	delay(0.001+Q);
	tone(Ab4,E+S);
	delay(0.001+E+S);
	tone(G4,S);
	delay(0.001+S);

	tone(Gb4,S);
	delay(0.001+S);
	tone(E4,S);
	delay(0.001+S);
	tone(F4,E);
	delay(0.001+E);
	delay(0.001+E);#PAUSE
	tone(Bb3,E);
	delay(0.001+E);
	tone(Eb4,Q);
	delay(0.001+Q);
	tone(D4,E+S);
	delay(0.001+E+S);
	tone(Db4,S);
	delay(0.001+S);

	tone(C4,S);
	delay(0.001+S);
	tone(B3,S);
	delay(0.001+S);
	tone(C4,E);
	delay(0.001+E);
	delay(0.001+E);#PAUSE QUASI FINE RIGA
	tone(F3,E);
	delay(0.001+E);
	tone(Ab3,Q);
	delay(0.001+Q);
	tone(F3,E+S);
	delay(0.001+E+S);
	tone(LA3,S);
	delay(0.001+S);

	tone(C4,Q);
	delay(0.001+Q);
	tone(LA3,E+S);
	delay(0.001+E+S);
	tone(C4,S);
	delay(0.001+S);
	tone(E4,H);
	delay(0.001+H);

	tone(LA4,Q);
	delay(0.001+Q);
	tone(LA3,E+S);
	delay(0.001+E+S);
	tone(LA3,S);
	delay(0.001+S);
	tone(LA4,Q);
	delay(0.001+Q);
	tone(Ab4,E+S);
	delay(0.001+E+S);
	tone(G4,S);
	delay(0.001+S);

	tone(Gb4,S);
	delay(0.001+S);
	tone(E4,S);
	delay(0.001+S);
	tone(F4,E);
	delay(0.001+E);
	delay(0.001+E);#PAUSE
	tone(Bb3,E);
	delay(0.001+E);
	tone(Eb4,Q);
	delay(0.001+Q);
	tone(D4,E+S);
	delay(0.001+E+S);
	tone(Db4,S);
	delay(0.001+S);

	tone(C4,S);
	delay(0.001+S);
	tone(B3,S);
	delay(0.001+S);
	tone(C4,E);
	delay(0.001+E);
	delay(0.001+E);#PAUSE QUASI FINE RIGA
	tone(F3,E);
	delay(0.001+E);
	tone(Ab3,Q);
	delay(0.001+Q);
	tone(F3,E+S);
	delay(0.001+E+S);
	tone(C4,S);
	delay(0.001+S);

	tone(LA3,Q);
	delay(0.001+Q);
	tone(F3,E+S);
	delay(0.001+E+S);
	tone(C4,S);
	delay(0.001+S);
	tone(LA3,H);
	delay(0.001+H);

	delay(2*H);


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