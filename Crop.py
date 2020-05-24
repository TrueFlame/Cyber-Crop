from Expanse import Expanse

class Crop(Expanse):
    def __init__ (self, crop_id: int, type: str, name: str, size: float, est_yield: str, longitude: str, latitude: str):
        self.crop_id = crop_id
        self.type = type
        self.name = name
        self.size = size
        self.est_yield = est_yield
        self.latitude = latitude
        self.longitude = longitude
