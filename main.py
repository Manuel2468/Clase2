from Empleado import *

empleados = []



e1 = Empleado()

e1.setNombre('Manuel')
e1.setApellido('Romero')
e1.setSueldo(1000000)
e1.setDiasLiquidados(10)
empleados.append(e1) #Ingreso de informacion en el arreglo

e2 = Empleado()

e2.setNombre('Angelica')
e2.setApellido('Franco Rojas')
e2.setSueldo(2500000)
e2.setDiasLiquidados(30)
empleados.append(e2) #Ingreso de informacion en el arreglo


for i in empleados:
    print('\n',i)

'''
print(e1.getNombre())
print(e1.getApellido())
print(e1.getSueldo())
'''