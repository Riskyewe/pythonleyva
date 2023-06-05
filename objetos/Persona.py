class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
        
p=Persona('Ana',123)
print(p.getNombre())
q=Persona('Pedro',321)
print(q.getNombre())