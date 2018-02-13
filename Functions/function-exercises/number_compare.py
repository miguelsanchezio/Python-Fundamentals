'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(a, b):
    if a > b:
        return 'First is greater'
    elif a < b:
        return 'Second is greater'
    else:
        return 'Numbers are equal'
