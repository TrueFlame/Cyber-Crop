class SensorSection():
    def __init__(self, Type, ID, Model, Install, Humidity, Temp, sun_exposure):
		self.Type=Type
		self.ID=ID
		self.Model=Model
		self.Install=Install
        	self.Humidity=Humidity
        	self.Temp=Temp
        	self.sun_exposure=sun_exposure
    
   def CheckPrivilege(AccountPrivilege):
		self.AccountPrivilege=AccountPrivilege
		if AccountPrivilege='Amateur':
			print("You don't have access to this category")
			print("Upgrade your account Or return to user menu")
       pass
   def ReturnPrivilege(AccountPrivilege):
		return AccountPrivilege
       pass
   def CheckSensor():
	if Install=False :
            print("There is an error in Sensor Installation")	
       pass
   def SensorInfo(expanse):
		self.Install=Install
		self.Humidity=Humidity
		self.Temp=Temp
		self.sun_exposure=sun_exposure
		print("Humidity:" Humidity, "Temperature:" Temp, "Sun Exposure: " sun_exposure)
       pass
   def SensorError():
		If Install = True:
			print("there is an error in Sensor system")
       pass


sensor = SensorSection(type,ID,Model)
info = SensorInfo(Humidity,Temp,sun_exposure)    
