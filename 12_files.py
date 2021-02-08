def read_file(fname):
    try:
        f =  open(fname,'rt')
        text = f.read()
    except FileNotFoundError:
        text = f'No existe el fichero {fname}'
    return text

print(read_file('sample.txt'))
print(read_file('samples.txt'))


try:
    file_name ='new_sample.txt'
    f = open(file_name,'xt')
    f.write('Esto es un fichero creado desde Python')
    print('El fichero se creo con exito', file_name)
    f.close()
except FileExistsError:
    print('El fichero ya existe.')

print(read_file(file_name))


import os
os.remove(file_name)
