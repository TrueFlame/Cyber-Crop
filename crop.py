class Crop:
    def __init__ (self, crop_id: int, type: str, name: str, size: float, est_yield: str, longitude: str, latitude: str):
        self.crop_id = crop_id
        self.type = type
        self.name = name
        self.size = size
        self.est_yield = est_yield
        self.latitude = latitude
        self.longitude = longitude
        
class Photovoltaics:
    def __init__ (self, id, model, type, production, efficiency):
        self.id = id
        self.model = model
        self.type = type
        self.production = production
        self.efficiency = efficiency

class Expanse:
    def __init__(self, exp_id: int, size: float, longitude: float, latitude: float):
        self.exp_id = exp_id
        self.size = size
        self. longitude = longitude
        self.latitude = latitude 
        self.crops = []
        self.photovoltaics = []
    
    def add_crop(self, crop_ob: Crop):
        self.crops.append({self.exp_id : crop_ob.crop_id})

    def add_photovoltaic(self, photo_ob: Photovoltaics):
        self.photovoltaics.append({self.exp_id : photo_ob.id})



expanse1 = Expanse(0, 500.3442, "7.634634", "9.8971489")

crop1 = Crop(2, "tulips", "Big Lips", "8.5m^2", "5 tons", "8.9789", "6.0980")
crop2 = Crop(1, "tomats", "Tomats", "345", "sth", "989", "egwg")

expanse1.add_crop(crop1)
expanse1.add_crop(crop2)
print(expanse1.crops)
