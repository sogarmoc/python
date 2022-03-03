# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 02/03/22

# Definicion de variables, diferencia mayus de minus

A = 10
a = 78
b = 12.45
C = 'Hola'

b, c, d = 2, 3.4, 'pepe'

# paso por valores que la variable x y z tienen el mismo valor
x = y = z = 'True'

# Variables constantes definirlas en mayusculas para diferenciarlas y no setearlas
PI = 3.1416

if __name__ == '__main__':
    print(PI)
    PI = 7
    print(PI)
    if a<c:
        print('El resultado es: ', a)

# Si se utiliza el + para concatenar varias cadenas si no son del mismo tipo hay que castearlo al mismo tipo str(), sino se utiliza la , y se podria concatenar de varios tipos


if __name__ == '__main__':
    print(type(C))
