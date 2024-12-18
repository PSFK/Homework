class Car:
    def __init__(self, model, year, engine_vol, price, mileage):
        self.model = model
        self.year = year
        self.engine_vol = engine_vol
        self.price = price
        self.mileage = mileage
        self.wheels = 4 #Стандартное кол-во колёс авто

    def description(self):
        return (f"Модель: {self.model}, Год выпуска: {self.year}, Объём двигателя: {self.engine_vol} л,"
                f"Цена: {self.price} руб., Пробег {self.mileage} км, Кол-во колёс {self.wheels}")

#Экземпляр класса авто
car_instance = Car("Toyota Camry", 2020, 2.5, 2000000, 30000)
print(car_instance.description())

class Truck(Car):
    def __init__(self, model, year, engine_vol, price, mileage):
        super().__init__(model, year, engine_vol, price, mileage)
        self.wheels = 8 #Стандартное кол-во колёс грузовик

#Экземпляр класса грузовик
truck_instance = Truck("Volvo FH", 2021, 12.8, 8000000, 150000)
print(truck_instance.description())