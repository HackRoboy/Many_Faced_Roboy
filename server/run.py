import telegramapp
import flaskapp
import threading
import roboy_interface

def main():
    telegramapp.main()
    flaskapp.app.run()
    roboy_interface.main()

if __name__ == '__main__':
    main()