class curso:
    def __init__(self,insertar,consultar,buscar,eliminar,modificar):
        self.__insertar=insertar
        self.__consultar=consultar
        self.__buscar=buscar
        self.__eliminar=eliminar
        self.__modificar=modificar
    def getInsertar(self):
        print("¿Nombre del curso?")
        insertar=input()
        return self.__insertar
    


a=curso   
print(a.getInsertar)