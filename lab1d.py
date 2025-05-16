#!/usr/bin/env python3

x = 10
y = 2
z = 5
ans = x+y*z 
#print(str(x) + ' + ' str(y) + ' * ' str(ans) + ' = ' + str(ans))
print (str(x) + ' + ' + str(y) + ' * ' + str(z) + ' = ' + str(ans))



#print(10 + 5) # addition
#print(10 - 5) # subtraction
#print(10 * 5) # multiplication
#print(10 / 5) # division
#print(10 ** 5) # exponents aka 'to the power of...'
#print(5 // 2) # integer division
#print(5 % 2) # returns remainder of integer division

# PEMDAS acronym, resolve the maths in order: 
''' (Parentheses (from inner most parentheses first, to the outermost, last), Exponents,
Multiplication and Division, Addition and Subtraction): '''

#print(10 + 5 * 2) # multiplication happens before addition, so 5*2 first, then 10 + the answer
#print((10 + 5) * 2) # parentheses happen before multiplication, so (10+5) first, then multiply by 2
#print(10 + 5 * 2 - 10 ** 2) # first exponents, then multiplication, then addition and subtraction from left to right
#print(15 / 3 * 4) # division and multiplication happen from left-to-right
#print(100 / ((5 + 5) * 2)) # the inner most parentheses are first performing addition, then parentheses again with multiplication, finally the division
#print()
#print()
#print()
