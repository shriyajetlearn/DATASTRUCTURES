class Car:
    def __init__(self, color, company, model, fuel_left):
        self.color = color
        self.company = company
        self.model = model
        self.fuel_left = fuel_left

    def get_company(self):
        return self.company

    def set_color(self, color):
        self.color = color

    def fill_fuel(self, fuel):
        self.fuel_left += fuel

    def show_car(self):
        print(f'This car is made by {self.company} and its model is {self.model}. Its {self.color} in color and has {self.fuel_left}% fuel left,')


car_a = Car('blue', 'Mercedes', 'S Class', 10)
car_a_company = car_a.get_company()
print(f'Company of Car A is {car_a_company}')
car_a.set_color('red')
car_a.show_car()

car_b = Car('yellow', 'Audi', 'A4', 0)
car_b.fill_fuel(100)
car_b.show_car()
