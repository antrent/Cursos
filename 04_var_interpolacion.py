lenguaje = 'Phyton'
autor = 'Guido'
msg = 'El lenguaje ' + lenguaje + ' fue creado por ' + autor
print(msg)

#es importante el orden de las variables asignaciones
i_msg = 'El lenguaje {} fue creado por {}'.format(lenguaje,autor)
print(i_msg)

#es importante el orden de las variables asignaciones
i_msg = 'El lenguaje %s fue creado por %s' % (lenguaje,autor)
print(i_msg)

#no importa el orden de las variables asignaciones
i_msg = 'El lenguaje {leng} fue creado por {autor}'.format(leng=lenguaje,autor=autor)
print(i_msg)

#importante el nombre de las variables
i_msg = f'El lenguaje {lenguaje} fue creado por {autor}'.format(leng=lenguaje,autor=autor)
print(i_msg)