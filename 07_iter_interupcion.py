animales = ['Perro','Gato','Canario','Pez']
i = 0
for animal in animales:
    if animal.lower() == 'pez':
        continue
    print(animal)
print('Final for Continue')    
print('===================')    

passw = 'pez'
usuPass = ''
i = 1
while (usuPass != passw):
    usuPass = input('Escriba la contraseña: ')
    if i >= 3:
        print('Demasiados intentos')
        break
    i += 1
else:
    print('Saludo, ya estas dentro')    


for animal in animales:
    if animal.lower() == 'pez':
        continue
    print(animal)    