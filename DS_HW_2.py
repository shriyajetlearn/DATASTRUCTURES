class Car:
    def __init__(self, color, company, model, fuel_left):
        self.color = color
        self.company = company
        self.model = model
        self.fuel_left = fuel_left

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def fill_fuel(self, fuel):
        self.fuel_left += fuel

    def show_car(self):
        print(f'This car is made by {self.company} and its model is {self.model}. Its {self.color} in color and has {self.fuel_left}% fuel left')


class Sedan(Car):
    def __init__(self, color, company, model, fuel_left, transmission, turbo):
        Car.__init__(self, color, company, model, fuel_left)
        self.transmission = transmission
        self.turbo = turbo
    def show_car(self):
        print(f'This car is made by {self.company} and its model is {self.model}. Its {self.color} in color and has {self.fuel_left}% fuel left. Transmission: {self.transmission}, Turbo: {self.turbo}')

bmw_3_series = Sedan('Black', 'BMW', '3 Series', 90, 'Automatic', True)
car_color = bmw_3_series.get_color()
print(car_color)
bmw_3_series.set_color('Yellow')
car_color = bmw_3_series.get_color()
print(car_color)

bmw_3_series.show_car()
