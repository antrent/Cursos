animales = ['Perro','Gato','Canario','Pez']
print(animales)
print(animales[0])
#print(animales[10]) --> error 
print(animales[0:2])

i = animales.index('Pez')
print(i)

animales[i] = 'Gallina'

print(animales)

animales.remove('Gato')
print(animales)

animales.insert(2,'Gato')
print(animales)

animales.remove('Gato')
item = animales.pop(1)
print(animales)
print(item)

cadena = 'Un anillo para gobernarlos a todos'

lista = cadena.split(' ')
print(lista)
cadena2 = ''.join(lista)
print(cadena2)

cadena2 = ''.join(lista)

tanimales = tuple(animales)
print(tanimales)
print(tanimales.count('Gato'))
print('Gato' in tanimales)
