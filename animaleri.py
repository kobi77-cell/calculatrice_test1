from client import Client
from animal import Animal
class Animaleri:
    def __init__(self, adresse):
        self.adresse = adresse

    def get_all(self):
        client = Client()
        return {
            "client": client.get()
        }

d = Animaleri(adresse="")
d.get_all()