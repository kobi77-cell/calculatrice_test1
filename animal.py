import random
import string

def generate():
    two_chiffre = str(random.randint(10,99))
    lettre = random.choice(string.ascii_uppercase)
    return f"{lettre}{two_chiffre}"

class Animal:
    def __init__(self, id, name, race):
        self.id = id
        self.name = name
        self.race = race

    def crie(self):
        print("JE CRIE FORT")
        print(f"L'animal {self.name} crie")


def add_animal(n):
    liste = []
    for i in range(0, n):
        id = generate()
        name = input("Enter Name: ")
        race = input("Enter race: ")
        print("\n")
        animal = Animal(id, name, race)
        liste.append(animal)
    return liste

def display_animal(liste_animal):
    if not liste_animal:
        print("Aucun animal à afficher.")
        return
    print("\n----- LISTE DES Animaux -----\n")
    for pets in liste_animal:
        data = pets.get()
        print(f"ID : {data['id']}")
        print(f"Nom : {data['name']}")
        print(f"Race : {data['race']}")
        print("------------------------------")


n = int(input("entrez un nombre:"))

liste1 = add_animal(n)
display_animal(liste1)