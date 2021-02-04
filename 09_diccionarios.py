animales = ['Perro','Gato','Canario','Pez']

animales_dic = {'Perro':'Guauu','Gato':'miauu','Canario':'pio','Pez':'hola'}
animales_dic2 = dict(Perro = 'guau', Gato = 'miauu')

print(animales_dic)
print(animales_dic2)

print(animales_dic2.items())
print(animales_dic2.keys())
print(animales_dic2.values())


for k, v in animales_dic.items():
        print(f'El {k} dice {v}')
print('Final For con el diccionario')

print(animales_dic['Perro'])
#print(animales_dic['Caballo']) => error KeyError

print(animales_dic.get('Gato'))
print(animales_dic.get('Caballo'))
animales_dic['Caballo']='Hiii'
print(animales_dic)


item = animales_dic.pop('Caballo')
print(animales_dic)
print(item)


