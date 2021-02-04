i = 0
while i <= 5:
    print(i)
    i += 1
print('Final While')

print('----------------')

for i in range(0,6):
    print(i)
print('Final For')
print('----------------')


paises = ['España','Colombia','Francia']
i = 0
for item in paises:
    i += 1
    print(i,item)
print('Final For')
print('-----------------------')

user = {'nombre':'Pepe','edad':23,'IsAlumno':True}
for k, v in user.items():
    print(k,v)
print('Final For tupla')
print('===========================')

users = [{'nombre':'Pepe','edad':23,'IsAlumno':True},
         {'nombre':'Elena','edad':24,'IsAlumno':False}]
for user in users:
    for k, v in user.items():
        print(k,v)
    print('--------')    
print('Final For anidados')
