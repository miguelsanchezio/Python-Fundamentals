d = dict(a=1, b=2, c=3)
d.clear()

d2 = d.copy()
d == d2 # True
d is d2 # False

{}.fromkeys('a','b') # {'a': 'b'}
{}.fromkeys(['email'], 'unknown') # {'email': 'unknown'}

d.get('a') # 1
d['no_key'] # KeyError
d.get('no_key') # None

d.pop('a') # {'b': 2, 'c': 3}

d.popitem() # removes random item

d3 = {
    'd': 4
}
d3.update(d) # {'a': 1, b': 2, 'c': 3, 'd': 4} adds values and/or overwrites values