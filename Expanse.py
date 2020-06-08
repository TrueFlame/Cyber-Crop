from Camera import *
from Ideal_Crop import *
from Sensor import *
from Profit_Calculation import *

class Expanse:
    def __init__(self, owner_username: str, exp_id: int, size: float, longitude: float, latitude: float):
        self.owner_username = owner_username
        self.exp_id = exp_id
        self.size = size
        self.longitude = longitude
        self.latitude = latitude 
        self.crops = []
        self.photovoltaics = []

    def add_crop(self, crop_ob):
        self.crops.append({self.exp_id : crop_ob.crop_id})
        crop_ob.exp_id = self.exp_id

    def add_photovoltaic(self, photo_ob):
        self.photovoltaics.append({self.exp_id : photo_ob.id})

    def Improvement_Alteration(self):
        pass
    
    def Maximum_Utilization(self):
        pass
    
    
    def AreaSelect(self):
        print("Which expanse would you like to select? ")
        user_input = input()
        if user_input == "Crop":
            for i, crop in enumerate(self.crops):
                pass
        
        elif user_input == "Photovoltaics":
            for i, crop in enumerate(self.photovoltaics):
                pass
    
    def ExpanseOverview(frame):
        new_camera = Camera(1, "TX-8767", "Balalaika")
        new_camera.Expanse_Overview(frame)

class Crop(Expanse):
    def __init__ (self, crop_id, crop_type, crop_name, est_yield, size, longitude, latitude, Sensor_ob, exp_id = None, owner_username = None):
        super().__init__(owner_username, size, longitude, latitude, exp_id)
        self.crop_id = crop_id
        self.crop_type = crop_type
        self.crop_name = crop_name
        self.est_yield = est_yield
        self.Sensor_ob = Sensor_ob
        self.Humidity, self.Temp, self.sun_exposure = Sensor_ob.Humidity, Sensor_ob.Temp, Sensor_ob.sun_exposure

        
class Photovoltaics(Expanse):
    def __init__ (self, photo_id, ph_type, name, production, efficiency,  size, longitude, latitude, Sensor_ob, exp_id = None, owner_username = None):
        super().__init__(owner_username, size, longitude, latitude, exp_id)
        self.photo_id = photo_id
        self.ph_type = ph_type
        self.name = name
        self.production = production
        self.efficiency = efficiency
        self.Sensor_ob = Sensor_ob
        self.sun_exposure = Sensor_ob.sun_exposure



