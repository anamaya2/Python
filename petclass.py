'''
Name: Ana Maya
GitHub Link: https://github.com/anamaya2/Python/upload
'''


class Pet:
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    def get_kind(self):
        return self.kind
    
    def get_breed(self):
        return self.breed
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def set_breed(self, breed):
        self.breed = breed

    def set_kind(self, kind):
        self.kind = kind

    def print_details(self):
        print(f"Pet Name: {self.name}")
        print(f"Pet Kind: {self.kind}")
        print(f"Pet Breed: {self.breed}")

pet1 = Pet("Dog", "Golden Doodle", "Max")
pet2 = Pet("Cat", "Persian", "Garfield")
pet3 = Pet("Fish", "Goldfish", "Nemo")

print("Pet 1 Details:")
pet1.print_details()
print("\nPet 2 Details:")
pet2.print_details()
print("\nPet 3 Details:")
pet3.print_details()

print(f"Type of pet1: {type(pet1)}")
