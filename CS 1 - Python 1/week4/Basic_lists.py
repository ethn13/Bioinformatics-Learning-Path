# Fun with lists

# Create

my_list = []
print my_list

l = [1, 2, 3]
print l

l2 = ["Ethan", "David", "Rina", "Whitney", 4]
print l2

l3 = [[1, 2], ['a', 'b', 'c'], []]
print l3

# Access

print len(l), len(l2), len(l3)
print l3[0][1]
l4 = l2[1:]
print l4

# Update
l[-1] = 4
l3[2] = 2
print l
print l3