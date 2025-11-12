# #Exercise 1
# #Instructions
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
all_cats = [Bengal("Luna", 3), Chartreux("Oreo", 5), Siamese("Minac", 7)]
sara_pets = Pets(all_cats)
sara_pets.walk()
# #Exercise 2
# #Instructions

class Dog():
    def __init__(self, dog_name, dog_age, dog_weight):
        self.dog_name = dog_name
        self.dog_age = dog_age 
        self.dog_weight = dog_weight
    def bark(self):
        print(f'{self.dog_name} is barking')    
    def run_speed(self):
        return self.dog_weight / self.dog_age * 10
    def fight(self, other_dog):
        if self.run_speed() * self.dog_weight < other_dog.run_speed() * other_dog.dog_weight:
            print(f"{other_dog.dog_name} won the fight against {self.dog_name}!")
        elif self.run_speed() * self.dog_weight > other_dog.run_speed() * other_dog.dog_weight:
            print(f"{self.dog_name} won the fight against {other_dog.dog_name}!")
        else:
            print(f"The fight between {self.dog_name} and {other_dog.dog_name} is a draw!")

dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Max", 3, 25)
dog3 = Dog("Rocky", 6, 30)
dog1.bark()
print(dog2.run_speed())
dog1.fight(dog2)
dog3.fight(dog1)