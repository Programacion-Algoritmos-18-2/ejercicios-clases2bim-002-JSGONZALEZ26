class Persona(object):  # Creación de la clase Persona

    def __init__(self, n, ape, ed, cod, n1, n2):  # Constructor de la clase
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    def agregar_nombre(self, n):  # Métodos para agregar y obtener los atributos
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad

    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo

    def obtener_apellido(self):
        """
        """
        return self.apellido

    def obtener_nota1(self):
        return self.nota1

    def agregar_nota1(self, n):
        self.nota1 = n

    def obtener_nota2(self):
        return self.nota2

    def agregar_nota2(self, n):
        self.nota2 = n

    def __str__(self):  # Sobreescritura del método __str__
        return "%s - %s - %d - %d - %d - %d" % (
                                                self.nombre,
                                                self.apellido,
                                                self.edad,
                                                self.codigo,
                                                self.nota1,
                                                self.nota2)


class OperacionesPersona(object):  # Clase que realiza las operacines con los datos

    def __init__(self, listado):  # Constructor que recibe de parámetro a la lista de run3.py
        """
        """
        self.listado_personas = listado

    def obtener_promedioN1(self,):  # Obtención del promedio de la nota 1
        sumaN1 = 0  # Uso de variable local acumuladora
        for n in self.listado_personas:
            sumaN1 = sumaN1 + n.obtener_nota1()
        promedio = sumaN1 / len(self.listado_personas)  # Calculo del promedio
        return promedio  # Retorna el promedio

    def obtener_promedioN2(self,):  # Obtención del promdeio de la nota 2
        sumaN2 = 0
        for n in self.listado_personas:
            sumaN2 = sumaN2 + n.obtener_nota2()
        promedio = sumaN2 / len(self.listado_personas)
        return promedio

    def obtener_listado_personas(self, k, m):  # Creación y presentación de la lista nueva
        lista_nueva = []  # Lista nueva vacía
        cadena = ""  # Cadena vacía
        for n in self.listado_personas:
            if (k == n.obtener_nombre()[0]):
                lista_nueva.append(n)  # Uso de .append() para añadir los elementos a la lista nueva
        for g in lista_nueva:
            cadena = "%s%s -%s\n" % (  # Se añaden los elementos deseados de cada elementos de la lista
                    cadena,
                    g.obtener_nombre(),
                    g.obtener_apellido())
        return cadena  # Se retorna la cadena

    def __str__(self):
        cadena = ""
        for n in self.listado_personas:
            cadena = "%s%s - %s\n" % (
                cadena,
                n.obtener_nombre(),
                n.obtener_apellido())
        return cadena
