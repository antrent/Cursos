class Persona():
    ## metodo constructor o inicializador, siempre debe estar definido
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
        self._estudio = None
    ##Resto de metodos a implementar    
    def saludar(self):
        print(f'Hola soy {self.nombre}, y tengo  {self._edad} años')
    
    def saludar_a(self, alguien = 'amigo'):
        print(f'Hola {alguien}, soy  {self.nombre}, y tengo  {self._edad} años')

    ############################################## Geter and seter
    def edad(self, edad = None):
        if edad: self._edad = edad
        return self._edad

##############################################
p1 = Persona('Pepe',23)
p2 = Persona('Elena',32)

print(type(p1),p1.nombre)
print(type(p2),p2.nombre)

p1.saludar()
p2.saludar()
p2.saludar_a(p1.nombre)

print(p1._edad) #no debe ser utilizadow
##print(p1._estudio) AtributeError: no se pede acceder 
p1.nombre = 'Jose'
print(p1.nombre)

p1._edad = 24
print(p1.nombre,p1._edad)

