a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print(type(a))
print(a.pop())
a.append(100)
a.reverse()
print a
del a[4]
print a

# https://docs.python.org/3/tutorial/datastructures.html
#Dict
tel = {'jack': 4098, 'sape': 4139}
print tel['jack']



#list
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))