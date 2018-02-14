'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    clean_word = string.replace(' ', '').lower()
    if clean_word == clean_word[::-1]:
        return True
    return False