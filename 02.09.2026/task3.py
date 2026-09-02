class Car:
    def __init__(self):
        self._engine_temperature = 20
    
    def start_engine(self):
        self._engine_temperature = 90
        print("Двигатель прогрет")
    
    def drive(self):
        if self._engine_temperature >= 90:
            print("Поехали!")
        else:
            print("Двигатель не прогрет!")

car = Car()

print(f"Прямой доступ к _engine_temperature: {car._engine_temperature}")
print("Попытка ехать без прогрева:")
car.drive()
print("\nПрогреваем двигатель:")
car.start_engine()
print("Теперь едем:")
car.drive()