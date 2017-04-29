import telegramapp
import flaskapp
import threading
import roboy_interface

def main():
    telegramapp.main()
    roboy_interface.main()
    flaskapp.app.run(host="0.0.0.0")
    

if __name__ == '__main__':
    main()