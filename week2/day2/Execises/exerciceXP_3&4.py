# #EXecrcice 3
# #Create a PetDog class that inherits from Dog and adds training and tricks
from exercisesXP import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(args)
        print(f"{dog_names} all play together!")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.dog_name} {random.choice(tricks)}")
        else:
            print(f"{self.dog_name} is not trained yet!")

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

# #Exercice 4
# #Practice working with classes and object interactions by modeling a family and its members.
class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = [] 

    def born(self, first_name, age):
        person = Person(first_name, age, self.last_name)
        self.members.append(person)
        print(f"A new member was born: {first_name} {self.last_name}, {age} years old")

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member found with the name {first_name}.")

    def family_presentation(self):
        print(f"Family {self.last_name}:")
        for person in self.members:
            print(f"{person.first_name}, {person.age} years old")

my_family = Family("Smith")
my_family.born("Alice", 17)
my_family.born("Bob", 20)
my_family.born("Charlie", 12)
print()
my_family.family_presentation()
print()
my_family.check_majority("Bob")
my_family.check_majority("Alice")
# personne non existante
my_family.check_majority("Daniel")

        