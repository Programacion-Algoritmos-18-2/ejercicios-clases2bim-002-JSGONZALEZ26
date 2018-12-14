from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
sumaN1 = 0
sumaN2 = 0
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    sumaN1 = sumaN1 + p.obtener_nota1()
    sumaN2 = sumaN2 + p.obtener_nota2()
    if (p.obtener_nota1() < 15) or (p.obtener_nota2() < 15):
        print(p.obtener_nombre())
    pass
'''print(p)'''

promedioN1 = sumaN1 / len(lista)

promedioN2 = sumaN2 / len(lista)

print(promedioN1, promedioN2)
