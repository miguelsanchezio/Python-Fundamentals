try:
    foobar
except:
    print('Error')

d = {'name': 'Ricky'}
d['city']

def get(d, 'city'):
    try:
        return d[key]
    except KeyError:
        return None
