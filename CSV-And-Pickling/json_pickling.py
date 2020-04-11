import jsonpickle

class Pet:
    allowed = ["cat", "dog", "fish", "rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet.")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet.")
        self.species = species

cat = Pet("Wong", "cat")

with open("pet.json", "w") as file:
    frozen = jsonpickle.encode(cat)
    file.write(frozen)

with open("pet.json") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(contents)
    print(unfrozen.set_species("dog"))


