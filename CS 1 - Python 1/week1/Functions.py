#link: https://py2.codeskulptor.org/#user49_5crO7ivYkziLxy0_1.py

#computes the area of a triangle 
#remember: always write the purpose of the function on top the comment of the function
def triangle_area(base, height):
    area = (1.0/2)*base*height
    return area

a1 = triangle_area(3, 8)
print a1
a2 = triangle_area(14, 2)
print a2

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5/9.0)*(fahrenheit - 32)
    return celsius

#test!!
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print c1, c2

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2

#print hello, world!
def hello():
    print "Hello, world!"

#test
hello()
h = hello()
print h