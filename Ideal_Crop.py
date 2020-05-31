class Ideal_Crop:
    def __init__ (self, crop_name, ideal_temp_low, ideal_temp_high, ideal_humidity_low, ideal_humidity_high,  sun_exposure, ground_data, helpful_tips):
        self.crop_name = crop_name
        self.ideal_temp_low = ideal_temp_low
        self.ideal_temp_high = ideal_temp_high
        self.ideal_humidity_low = ideal_humidity_low
        self.ideal_humidity_high = ideal_humidity_high
        self.sun_exposure = sun_exposure
        self.ground_data = ground_data [:]
        self.helpful_tips = helpful_tips [:]

Tomato = Ideal_Crop("Tomato",1,10,2,20,30,["x","y","z"],["tip1","tip2","tip3"])
Potato = Ideal_Crop("Potato",1,10,2,20,30,["x","y","z"],["tip1","tip2","tip3"])
Cucumber = Ideal_Crop("Cucumber",1,10,2,20,30,["x","y","z"],["tip1","tip2","tip3"])
Green_Pepper = Ideal_Crop("Green Pepper",1,10,2,20,30,["x","y","z"],["tip1","tip2","tip3"])\

    def show_ideal_crop(crop_name):
        pass
    
