stuff = [5,3,7]

def do_stuff(stuff):
    """Trying to manually sorting  or bubble sorting"""
    n_items = len(stuff)
    for i in range(n_items):
        for j in range(i+1, n_items):
            if stuff[i] > stuff[j]:
                stuff[i], stuff[j] = stuff[j], stuff[i]

