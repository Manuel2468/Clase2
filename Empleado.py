
class Empleado:

    def __init__(self):
        self.__nombre = None #string o texto
        self.__apellido = None #string o texto
        self.__sueldo = None #float o decimal
        self.__diasliquidados = None #int o entero

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSueldo(self):
        return self.__sueldo

    def getDiasLiquidados(self):
        return self.__diasliquidados

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def setApellido(self, apellido:str):
        self.__apellido = apellido
    
    def setSueldo(self, sueldo:float):
        self.__sueldo = sueldo

    def setDiasLiquidados(self, dias:int):
        self.__diasliquidados = dias

    def SalarioDevengado(self):
        return self.__sueldo * int(self.__diasliquidados) / 30

    def __str__(self):
        return str('\nNombre: ' + self.__nombre +
                '\nApellido: ' + self.__apellido +
                '\nSueldo: ' + str(self.__sueldo) +
                '\nSalario Devengado:' + str(self.SalarioDevengado()))
