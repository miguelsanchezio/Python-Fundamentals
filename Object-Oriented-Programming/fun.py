class FunDict(dict):
    def __repr__(self):
        print("HERE YOU GO!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"WHOOPS! {key} DOESN'T EXIST!")

    def __setitem__(self, key, value):
        print("NOICE! LET'S CHANGE THE DICTIONARY!")
        super().__setitem__(key, value)


data = FunDict({"first": "Tom", "animal": "cat"})
print(data)