class FunDict(dict):
    def __repr__(self):
        print("HERE YOU GO!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"WHOOPS! {key} DOESN'T EXIST!")

    def __setitem__(self, key, value):
        print("NOICE! LET'S CHANGE THE DICTIONARY!")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("LET'S CHECK IF IT CONTAINS SOMETHING!")
        return super().__contains__(item)

data = FunDict({"first": "Tom", "animal": "cat"})
print(data)

print("first" in data)