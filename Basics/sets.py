'''
lists = []
tuples = ()
sets = {}
'''

a1 = {3,2,5,3,2,5,12}
a2 = {1,7,9}
#print(a1.pop())
a1.add(22)
print(a1.union(a2))
print(a1.intersection(a2)) # returns set because it's empty