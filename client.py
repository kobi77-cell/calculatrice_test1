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

class Client:
    def __init__(self, id, name, genre, tel):
        self.__id = id
        self._name = name
        self.genre = genre
        self._tel = tel
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


    def get(self):
        return {
            "id": self.__id,
            "name": self._name,
            "tel": self._tel
        }

    def set(self,name, tel):
        if name is not None:
            self._name = name
        if tel is not None:
            self._tel = tel


def display_client(liste_clients):
    if not liste_clients:
        print("Aucun client à afficher.")
        return

    print("\n----- LISTE DES CLIENTS -----\n")
    for client in liste_clients:
        data = client.get()
        print(f"ID : {data['id']}")
        print(f"Nom : {data['name']}")
        print(f"Téléphone : {data['tel']}")
        print("------------------------------")


# k= Client(id, name= None,genre = None,tel = None )


taille = int(input("n:"))

liste = add_client(taille)

display_client(liste)