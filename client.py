import random
import string

def generate_id():
    two_chiffre = str(random.randint(10,99))
    lettre = random.choice(string.ascii_uppercase)
    four_chiffre = str(random.randint(1000,9999))
    return f"{two_chiffre}{lettre}{four_chiffre}"

def add_client(n):
    liste1 = []
    for i in range(0, n):
        id = generate_id()
        name = input("Enter Name: ")
        genre = input("Enter genre: ")
        tel = int(input("Enter tel: "))
        print("\n")
        client = Client(id, name, genre, tel)
        liste1.append(client)
    return liste1

def display_client(liste1):
    print("\t==== LISTE DES CLIENTS ====\n")
    for j in range(len(liste1)):
       print(f"ID:: {liste1.id}, Name : {liste1.name}")




class Client:
    def __init__(self, id, name, genre, tel):
        self.__id = None
        self.__name = name
        self.genre = genre
        self.__tel = tel
        self.liste1 = []

    # def add_client(self, lent):
    #     for i in range(0, lent):
    #         self.id = generate_id()
    #         self.name = input("Enter Name: ")
    #         self.genre = input("Enter genre: ")
    #         self.tel = int(input("Enter tel: "))
    #         print("\n")
    #         self.liste1.append(self.liste1)
    #
    # def display(self):
    #     for liste in range(len(self.liste1)):
    #         print(f"  {self.id}:\n --Name: {self.name}\n --Genre: {self.genre}\n --Tel: {self.tel}\n")


    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_tel(self):
        return self.__tel

    def set_name(self, name):
        self.__name = name
    def set_tel(self, tel):
         self.__tel = tel


# k= Client(id, name= None,genre = None,tel = None )


taille = int(input("n:"))

liste = add_client(taille)