def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
         print('Error no se puede dividir por 0')    
    except Exception as err:
         print('Error', type(err).__name__)

print(dividir(7,2))
r = dividir(7,0)
#if not not r: print(r)
if r != None: print(r)

try:
    print(dividir(7,0))
except TypeError as err:
    print('Error',type(err).__name__)
    


