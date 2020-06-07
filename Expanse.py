from Camera import *
from Ideal_Crop import *
from Sensor import *
from Profit_Calculation import *

class Expanse:
    def __init__(self, owner_username, exp_id: int, size: float, longitude: float, latitude: float):
        self.owner_username = owner_username
        self.exp_id = exp_id
        self.size = size
        self. longitude = longitude
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
    
    def ReturnErrocCode(self):
        return False
    
    def ReturnErrorMessage(self):
        print("Expanse does not exist")
    
    def ReturnBestMessage(self):
        print("Successful Add")
    
    def ChooseOption(self):
        pass
    
    def AreaSelect(self):
        print("What would you like to select ? ")
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
    def __init__ (self, crop_id: int, crop_type: str, name: str, size: float, est_yield: float, longitude, latitude, exp_id = None):
        super().__init__(longitude, latitude)
        self.crop_id = crop_id
        self.crop_type = crop_type
        self.name = name
        self.size = size
        self.est_yield = est_yield
        self.exp_id = exp_id
        
class Photovoltaics(Expanse):
    def __init__ (self, photo_id: int, model: str, ph_type: str, production: float, efficiency: int, longitude: float, latitude: float, exp_id = None):
        super().__init__(longitude, latitude)
        self.photo_id = photo_id
        self.model = model
        self.ph_type = ph_type
        self.production = production
        self.efficiency = efficiency
        self.exp_id = exp_id


expanse1 = Expanse("andy", 1, 1000.0, 9.98789 , 9.070709)
crop1 = Crop(1, "Orange", "My Oranges", 150, 150.0, 9.89986, 9.00785568)

expanse1.add_crop(crop1)

country1, currency1 = ChooseParameters()

profit_calculator = ProfitCalculation(1, country1, currency1)

