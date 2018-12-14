from paquete_archivos.miarchivo import MiArchivo  # Importación de MiArchivo.py
from paquete_modelo.mimodelo import Persona, OperacionesPersona  # Importación de las clases

m = MiArchivo()  # Creación de objeto
lista = m.obtener_informacion()  # Creación de lista
lista = [l.split("|") for l in lista]  # Separar los elementos con el uso de .split()

# print(lista)

lista = lista[1:]  # La lista inicia desde la posición 1
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
lista_persona = []  # Lista nueva vacía
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])  # Creación del objetos de clase Persona
    lista_persona.append(p)  # Los objetos se vuelven elementos de la lista

operaciones = OperacionesPersona(lista_persona)  # Creación de un objeto de clase OperacionesPersona
print(operaciones.obtener_promedioN1())  # Imprimir el promedio 1
print(operaciones.obtener_promedioN2())  # Imprimir el promedio 2
print(operaciones.obtener_listado_personas("R", "J"))  # Imprimir la lista con la condición de R o J
