# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 03/03/22

# Declaracion de variables

a = 2
b = 5
c = 'Hola'
d = 6.4

# Output de datos

if __name__ == '__main__':
    print('Valor de a: ', a)
    print('Valor de b: ', b)
    print('Valor de c: ', c)
    print('Valor de d: ', d)
    b = c
    print('B tome el valor de C: ', b)
    c = a
    print('C tome el valor de A: ', c)
    a = d
    print('A tome el valor de D: ', a)
    d = b
    print('D tome el valor de B: ', d)