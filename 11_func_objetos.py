def suma(a, b): # parametros 
    r = a + b
    return r

def resta(a, b): # parametros 
    r = a - b
    return r
print(type(suma))
y = suma
print(y(3,6))

def calcular(a, b, callback ):
    print(callback(a,b))

calcular(3,8, suma)
calcular(3,8, resta)
calcular(3,8, lambda a,b:a*b)
div = lambda a,b:a*b
print(div(3,5))

def multiplicador(n):
    return lambda a : a * n

duplicar = multiplicador(2)
triplicador = multiplicador(3)

print(duplicar(12))
print(triplicador(12))
