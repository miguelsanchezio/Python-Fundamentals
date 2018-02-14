'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(li, cmd, loc, val=None):
    if cmd == 'remove' and loc == 'end':
        return li.pop()
    elif cmd == 'remove' and loc == 'beginning':
        return li.pop(0)
    elif cmd == 'add' and loc == 'beginning':
        li.insert(0, val)
        return li
    elif cmd == 'add' and loc == 'end':
        li.append(val)
        return li
    