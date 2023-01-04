# -*- coding: utf-8 -*-
from Base import Base

class Fabricante(Base):
    def __init__(self, nombre=" " , pais = " "):
        self.__nombre = nombre
        self.__pais = pais
        
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais


    def __str__(self):
        
        resp = '\t Nombre: ' + str(self.nombre) + '\n'
        resp = resp +'\t Pais: ' + str(self.pais)
        return resp
    
    def Captura(self):
        self.nombre = (input("Nombre del Fabricante: "))
        self.pais = (input("Pais del Fabricante:: "))
        
        
class Proveedor(Fabricante):
    def __init__(self,  nombre=" " , pais = " ", codigo = " ", indice = 0 ):
        super().__init__( nombre, pais)
        self.__codigo = codigo
        self.__indice = indice

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @property
    def indice(self):
        return self.__indice

    @indice.setter
    def indice(self, indice):
        self.__indice = indice
    
    def __str__(self):
            resp = "\n---------------Proveedor--------------\n"
            resp += super().__str__()
            resp += '\n \t Codigo: ' + str(self.codigo) + ' '
            resp += '\n \t Indice Calidad: ' + str(self.indice) + ' \n'
            return resp
        
    def Captura(self):
        super().Captura()
        self.codigo = (input("Codigo proveedor : "))
        self.indice = int(input("indice de Calidad del proveedor: "))
        
        

class Fabricante_Original(Fabricante):
    def __init__(self,  nombre=" " , pais = " ", direccion = " ", telefono = " ", email = " " ):
        super().__init__( nombre, pais)
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion
        
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
        
        
    def __str__(self):
            resp = "\n--------------------Fabricante Original-------------------\n"
            resp += super().__str__()
            resp += '\n \t Direccion: ' + str(self.direccion) + ' \n'
            resp += '\n \t Telefono: ' + str(self.telefono) + ' \n'
            resp += '\n \t Email: ' + str(self.email) + ' \n'
            resp += "\n--------------------------------------------------------\n"
            return resp
        
    def Captura(self):
        super().Captura()
        self.direccion = (input("Direccion del Fabricante: : "))
        self.telefono = int(input("Telefono del Fabricante: : "))
        self.email = input("Email del Fabricante: : ")
        
        
        


"""

fab = Fabricante("Julio","CR")
prov = Proveedor("Julio","CR","G4D14",75)
fabO = Fabricante_Original("Julio","CR","San Jose","22564741","jul@gmail.com")
fabO.Captura()
#feN = fe.Captura()

print(fabO.__str__())

"""