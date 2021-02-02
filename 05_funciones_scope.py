def prueba(c):
    c = 'Juan'
    d = 'Pedro'
    print('Dentro de la funcion c vale',c)
    print('Dentro de la funcion d vale',d)
    print('Dentro de la funcion a vale',a)

c = 'Carlos'
a = 'Ernesto'
prueba('')
print('Fuera de la funcion c vale',c)


def prueba_lista(c):
    c[0] = 'Juan'
    print('Dentro de la funcion c vale',c)

c = ['Carlos','Maria']
prueba_lista([*c])
print('Fuera de la funcion c vale',c)