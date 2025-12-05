a = 12
b = 3

print( a + b)
print( a - b)
print( a * b)
print( a / b)
print( a // b) # integer division 
print(a % b)

for i in range( 1, 10):  #here in range instead of 10 we can't use a / b as float is not considered an integer :) but we can use a // b as it is a int
    print(i)

print(a + b / 3 - 4 * 12)
print(a + (b/3) - (4 * 12)) # bodmas
print((((a + b) / 3) - 4) * 12) #due to parenthesis we can get the result acc. to our need 
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4

print(e * 12)
