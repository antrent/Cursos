x = '12'
y = 3
z = 4
print(x,type(x))
print(y,type(y))
print(z,type(z))

# Tipado debil (JS) - casting implicito
print('y + z',y + z)

# Tipado fuerte - no hay casting implicito
#TypeError: can only concatenate str (not "int") to str
#print('x + y',x + y)

print('x + y',x + str(y))
print('x + y',int(x) + y)

a = 12
b = 2.4
c = 0
print(a,type(a))
print(b,type(b))

print('a * b',a * b)

print(not not a)
print(not not c)