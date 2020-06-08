class Ideal_Crop:
    def __init__ (self, crop_name, ideal_temp_low, ideal_temp_high, ideal_humidity_low, ideal_humidity_high,  sun_exposure, ground_data : list, helpful_tips: list):
        self.crop_name = crop_name
        self.ideal_temp_low = ideal_temp_low
        self.ideal_temp_high = ideal_temp_high
        self.ideal_humidity_low = ideal_humidity_low
        self.ideal_humidity_high = ideal_humidity_high
        self.sun_exposure = sun_exposure
        self.ground_data = ground_data
        self.helpful_tips = helpful_tips


    def show_ideal_crop(self):
        print(self.crop_name)
        print(self.ideal_temp_low)
        print(self.ideal_temp_high)
        print(self.ideal_humidity_low)
        print(self.ideal_humidity_high)
        print(self.sun_exposure)
        print(self.ground_data)
        print(self.helpful_tips)


crop_strawberries = Ideal_Crop("Strawberry", 15, 26, 0.65, 0.75, 700, ["Well-draining soil", "Slightly Acidic"], ["Give them some space!", "Plant in a sunny area",  "Don’t drown the strawberries", "Plant a variety"])
crop_oranges = Ideal_Crop("Orange", 13, 36, 0.5, 0.6, 600, "High pineland soil", ["Prune in spring or summer to shape plants", "Very sweet oranges need a long season of warm weather", "Pick when richly colored and fully ripe", "Grow outdoors in the warmer months to expose plants to heat and pollinators"])

crop_eggplants = Ideal_Crop("Eggplant", 21, 30, 0.5, 0.65, 750, "Slightly Acidic", ["Choose a very sunny spot for the best results.", "Eggplant grows best in a well-drained sandy loam or loam soil, fairly high in organic matter.", "Soil pH should be between 5.8 and 6.5 for best growth.", "Use a covering of black plastic mulch to warm soils before setting out transplants."])
