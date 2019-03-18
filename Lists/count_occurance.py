def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])
    
a = (5,2,3,3,4,5,5,5,6,5,6,4,2,3,3,3,4,5,6,7,5,4)

howmany = count_occurrences(a, 5)
print("there are: {}".format(howmany))
