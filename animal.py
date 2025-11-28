import random
import string

def generate_id():
    two_chiffre = str(random.randint(10,99))
    lettre = random.choice(string.ascii_uppercase)
    return f"{lettre}{two_chiffre}"

def add_animal(n):
    liste = []
    for i in range(0, n):

        name = input("Enter Name: ")
        race = input("Enter Race: ")

        animal1 = Animal(name, race)
        liste.append(animal1)
    return liste

class Animal:
    def __init__(self, id, name, race):
        self.id = None
        self.name = name
        self.race = race

    def crie(self):
        print("JE CRIE FORT")
        print(f"L'animal {self.name} crie")




