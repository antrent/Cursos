def suma(a, b): # parametros 
    r = a + b
    return r

#print(r) -> no aconsejado mala practica por mesclar operaciones
def suma_y_muestra(a, b):
    r = a + b
    print(r)

indice = 6    
print(suma(3,indice)) # invoca funcion pasando los parametros

suma_y_muestra(3,9)

def suma_vd(a = 0, b = 0): # parametros 
    r = a + b
    return r
print(suma_vd(2))    
# No es permitido 
#print(suma_vd(,2))    
print(suma_vd())
