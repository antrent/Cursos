x = 3
print(x,type(x), id(x))

l = ['pepe','juan', 'elena']
print(l,type(l), id(l))

#Las variables son Inmutables = todas tienen una nueva referencia
# Se ellimina la referencia de 3 y se crea una nueva para 23
x = 23
print(x,type(x), id(x))

# Son variable mutables y por lo tanto cambian sin cambiar de referencia
l[0] = 'Jose' 
print(l,type(l), id(l))