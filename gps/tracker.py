from cacher import mcache
from time import sleep
import urllib.parse, urllib.request


def main():
	with open("gps.txt","w+") as f:
		f.write("type\tlatitude\tlongitude\tname\tdesc\n")
	
	while True:
		gpsdata = mcache.gps
		print(gpsdata)
		if "$GPGGA" not in gpsdata:
			print("No gps yet!")
			continue
		with open("gps.txt","a+") as f:
			try:
				lat = float(gpsdata["$GPGGA"][1])
				lon = float(gpsdata["$GPGGA"][3])
				text = "T\t{lat}\t{lon}\n".format(lat = lat, lon = lon)
				print(text)
				f.write(text)
			except:
				print("Cant read gps")
		
		with open("gps.txt","r") as f:
			fdata = urllib.parse.quote(f.read())
			seturl = "http://themagnificentcacher.appspot.com/set/{name}/{data}"
			try:
				urllib.request.urlopen(seturl.format(name = "tracker", data=fdata)).read()
			except:
				pass
		sleep(5)
		

if __name__ == '__main__':
	main()