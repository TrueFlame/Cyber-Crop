from expanse import Expanse

class Crop(Expanse):
    def __init__ (self, crop_id: int, type: str, name: str, size: float, est_yield: str, longitude: str, latitude: str):
        self.crop_id = crop_id
        self.type = type
        self.name = name
        self.size = size
        self.est_yield = est_yield
        self.latitude = latitude
        self.longitude = longitude
        


crop3 = Crop(3, 'hth', "name", "size", "est_yield", "longitude", "latitude")

expanse2 = Expanse(3, 8.0975, "676", "67568")

expanse2.add_crop(crop3)
print(expanse2.crops)
