# #Execice 1
# #Instruction
# #Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Oreo", 6)
cat2 = Cat("Minac", 8)
cat3 = Cat("Luna", 1)

def find_oldest_cat(cat1, cat2, cat3):
    oldest = max(cat1, cat2, cat3, key=lambda cat: cat.age)
    return oldest

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
# #Execice 2
# #Instruction
# #Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.
class Dog():
    def __init__(self, name_dog, height_dog):
        self.name_dog = name_dog
        self.height_dog = height_dog

    def bark(self):
        print(f"{self.name_dog} goes woof!")
    def jump(self):
        print(f"{self.name_dog} jumps {self.height_dog*2}cm high!")

davids_dog = Dog("Rex", 15)
sarahs_dog = Dog("Snow", 12)
print(f"David's dog name is {davids_dog.name_dog} and it's height {davids_dog.height_dog}")
print(f"Sarah's dog name is {sarahs_dog.name_dog} and it's height {sarahs_dog.height_dog}")  
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height_dog > sarahs_dog.height_dog:
    print(f"{davids_dog.name_dog} is bigger than {sarahs_dog.name_dog}")
elif davids_dog.height_dog < sarahs_dog.height_dog:
    print(f"{sarahs_dog.name_dog} is bigger than {davids_dog.name_dog}")
else:
    print(f"{davids_dog.name_dog} and {sarahs_dog.name_dog} are the same size!")
# #Execice 3
# #Instruction
# #Create a Song class with a method to print song lyrics line by line.
class Song():
    def __init__(self, lyrics = []):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for word in self.lyrics:
            print(word)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# #Execice 4
# #Instruction  
# # cla
class Zoo():
    def __init__(self, zoo_name, animals=[]):
        self.zoo_name = zoo_name
        self.animals = animals

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        print("Animals in the zoo:", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} not found in the zoo.")

    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)

        self.grouped_animals = grouped_animals
        return grouped_animals

    def get_groups(self):
        if hasattr(self, "grouped_animals"):
            for letter, group in self.grouped_animals.items():
                print(f"{letter}: {group}")
        else:
            print("Animals have not been sorted yet. Call sort_animals() first.")
brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
