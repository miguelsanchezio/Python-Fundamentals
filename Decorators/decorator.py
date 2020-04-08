def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")

    return wrapper


@be_polite
def greet():
    print("My name is Alex")


# greet = be_polite(greet)
greet()


@be_polite
def loud():
    print("MY NAME IS ALEX")


loud()
