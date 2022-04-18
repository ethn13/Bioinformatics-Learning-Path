# Mutable and immutable objects in python
# Lists are the only mutable objects in python

a = 1
print(id(1))
print(id(a))
a = 2
print(id(2))
print(id(a))

l = [1, 2]
print(id(l))
l[0] = 0
print(id(l))
print ""

print 1 is 1
print 1.0 is 1.0
print True is True
print "abc" is "abc"
print [4,5] is [4, 5]


# 