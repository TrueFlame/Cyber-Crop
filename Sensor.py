#import RPi.GPIO as GPIO
import random
#import Adafruit_DHT # arduino library

#from RPLCD import CharLCD # arduino library

#lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])


#GPIO SETUP
channel = 21 # for nonexistent arduino sensor
#GPIO.setmode(GPIO.BCM) # added for more truthfulness
#GPIO.setup(channel, GPIO.IN)
 
class Sensor():
    def __init__(self, Type, ID, Model, Installation = None):
        self.Type=Type
        self.ID=ID
        self.Model=Model
        self.Installation = self.diagnosis()
        self.Humidity, self.Temp, self.sun_exposure = self.get_data()

    def CheckSensor(self):
        if self.Installation == True:
            print("There is no error in Sensor Installation")
        else:
            self.SensorError()

    def SensorInfo(self):
        print("Humidity:" + self.Humidity, "Temperature:" + self.Temp, "Sun Exposure: " + self.sun_exposure)
        pass
    
    def SensorError(self):
        if not self.Installation:
            print("There is an error in the Sensor Installation")

    def get_data(self):
        #humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        humidity = round(random.random(), 2)
        temperature = round(random.uniform(5.0, 40.0), 2)
        sun_exposure = round(random.randint(300, 1000), 2)
        return humidity, temperature, sun_exposure
        
    def diagnosis(self):
        if channel != 21:
            print (" Nothing is running")
            return False
        else:
            print ("Sensor is working!")
            return True
    
