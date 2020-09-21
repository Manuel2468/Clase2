
class Empleado:

    def __init__(self):
        self.nombre = None #string o texto
        self.apellido = None #string o texto
        self.sueldo = None #float o decimal

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getSueldo(self):
        return self.sueldo

    def setNombre(self, nombre:str):
        self.nombre = nombre

    def setApellido(self, apellido:str):
        self.apellido = apellido
    
    def setSueldo(self, sueldo:float):
        self.sueldo = sueldo