from Expanse import Expanse

class Photovoltaics(Expanse):
    def __init__ (self, id, model, type, production, efficiency):
        self.id = id
        self.model = model
        self.type = type
        self.production = production
        self.efficiency = efficiency
