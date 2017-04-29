import telegramapp
import flaskapp
import threading

def main():
    telegramapp.main()
    flaskapp.app.run(debug=True)

if __name__ == '__main__':
    main()