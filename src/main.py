class Bikes():
    engine = 49
    type = 'scooter'
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model



bike1 = Bikes("Honda", 'Super cub')

print(bike1.engine)
