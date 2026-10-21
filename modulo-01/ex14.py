# Método com variável auxiliar
a = 10
b = 20

aux = a
a = b
b = aux

print(a, b)

# Metodo idiomatico 
c = 10
d = 20

c, d = d, c

print(c, d)