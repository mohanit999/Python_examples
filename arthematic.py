#Arithematic operators
a, b = input('Enter a and b are ').split(',')
a=int(a)
b=int(b)
a+=5
print('addition',a+b)
print('subtraction',a-b)
print('multiplication',a*b)
print('division',a/b)
print('flooring',a//b)
print('remainder',a%b)
print('power',a**b)

#Relational operators
print('equals',a==b)
print('greaterthan',a>b)
print('lessthan',a<b)
print('greaterthan are equals',a>=b)
print('lessthan are equals',a<=b)
print('not equal', a!=b)

#Assignment Operators
print(a)
a-=5
print(a)
a*=5
print(a)
a/=b
print(a)
a//=b
print(a)
a%=b
print(a)
b**=3
print(b)
