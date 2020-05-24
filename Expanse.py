from Account import *
from tkinter import *
from tkinter import ttk
from Photovoltaics import *
from Crop import *

class Expanse:
    def __init__(self, exp_id: int, size: float, longitude: float, latitude: float):
        self.exp_id = exp_id
        self.size = size
        self. longitude = longitude
        self.latitude = latitude 
        self.crops = []
        self.photovoltaics = []
    
    def add_crop(self, crop_ob):
        self.crops.append({self.exp_id : crop_ob.crop_id})

    def add_photovoltaic(self, photo_ob):
        self.photovoltaics.append({self.exp_id : photo_ob.id})

    def Improvement_Alterration():
        pass
    
    def Maximum_Utilization():
        pass
    
    def ChooseExpanse():
        pass
    
    def ReturnErrocCode():
        pass
    
    def ReturnErrorMessage():
        pass
    
    def ReturnBestMessage():
        pass
    
    def ChooseOption():
        pass
    
    def AreaSelect():
        pass
    
    def ExpanseOverview():
        pass

    def printsth(self):
        print("Hell yeah")







expanse1 = Expanse(0, 500.3442, "7.634634", "9.8971489")

crop1 = Crop(2, "tulips", "Big Lips", "8.5m^2", "5 tons", "8.9789", "6.0980")
crop2 = Crop(1, "tomats", "Tomats", "345", "sth", "989", "egwg")
