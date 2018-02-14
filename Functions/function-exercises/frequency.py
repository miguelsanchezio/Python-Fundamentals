'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(li, search_term):
    return li.count(search_term)