class crop():
    def __init__(self, crop_id, type, name, size, est_yield): # this is the correct way
		self.crop_id = crop_id
		self.type = type
		self.name = name
		self.size = size
		self.est_yield = est_yield
    
    subject_a = crop(1, tomato, 90, 1.09)
