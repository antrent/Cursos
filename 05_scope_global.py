g = 1

def use_global():
    global g
    g = g + 5
    print('Dentro g vale ',g)

use_global()
print('fuera g vale ',g)