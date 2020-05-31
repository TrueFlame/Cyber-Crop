class SensorSection():
    def __init__(self, Type, ID, Model, Install, Humidity, Temp, sun_exposure):
        self.Type=Type
        self.ID=ID
        self.Model=Model
        self.Install=Install
        self.Humidity=Humidity
        self.Temp=Temp
        self.sun_exposure=sun_exposure
    
    def CheckSensor():
        if Install == False:
            print("There is an error in Sensor Installation")	
            pass
    def SensorInfo(expanse):
              print("Humidity:" +Humidity, "Temperature:" +Temp, "Sun Exposure: " +sun_exposure)
              pass
    def SensorError():
        if Install == True:
            print("there is an error in Sensor system")
            pass


sensor = SensorSection(type,ID,Model)
info = SensorInfo(Humidity,Temp,sun_exposure)    
