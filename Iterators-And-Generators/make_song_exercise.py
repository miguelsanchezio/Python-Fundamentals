def make_song(count=99, beverage="soda"):
    while count >= 0:
        if count > 1:
            i = count
            count -= 1
            yield "{} bottles of {} on the wall.".format(i, beverage)
        elif count == 1:
            count -= 1
            yield "Only 1 bottle of {} left!".format(beverage)
        elif count == 0:
            count -= 1
            yield "No more {}!".format(beverage)

def make_song_2(count=99, beverage="soda"):
    for num in range(count, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        elif num == 0:
            yield "No more {}!".format(beverage)

k_song = make_song(5, "kombucha")

print(next(k_song))
print(next(k_song))
print(next(k_song))
print(next(k_song))
print(next(k_song))
print(next(k_song))
print(next(k_song))