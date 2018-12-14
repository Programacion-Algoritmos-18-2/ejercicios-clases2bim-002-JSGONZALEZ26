import codecs  # Importación de codecs


class MiArchivo:  # Creación de la clase para el manejo de archivos
    """
    """

    def __init__(self):  # Constructor
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r")  # Lectura del archivo

    def obtener_informacion(self):  # Leer los elementos del archivo
        return self.archivo.readlines()

    def cerrar_archivo(self):  # Cerrar el archivo
        self.archivo.close()


class MiArchivoEscribir:  # Creación de clase para edición del archivo
    """
    """

    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a")  # Modificación o Creación de nuevo archivo

    def agregar_informacion(self, p):  # Agregar información al archivo
        self.archivo.write("%s-%s-%d-%d\n" % (
            p.nombre,
            p.apellido,
            p.edad,
            p.codigo))

    def cerrar_archivo(self):  # Cerrar el archivo
        self.archivo.close()
