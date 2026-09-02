class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

cat1 = Cat("Сиамская", "Барсик", 3)
cat2 = Cat("Персидская", "Мурка", 5)
cat3 = Cat("Британская", "Пушок", 2)

print(f"Кот 1: {cat1.name}, порода {cat1.breed}, возраст {cat1.age} лет")
print(f"Кот 2: {cat2.name}, порода {cat2.breed}, возраст {cat2.age} лет")
print(f"Кот 3: {cat3.name}, порода {cat3.breed}, возраст {cat3.age} лет")