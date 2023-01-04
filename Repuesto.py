# -*- coding: utf-8 -*-
from Base import Base

class Repuesto(Base):
    def __init__(self, codigo=" " , nombre = " ", precio = 0.0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio


    def __str__(self):
        
        resp = '\t Codigo: ' + str(self.codigo) + '\n'
        resp = resp +'\t Nombre: ' + str(self.nombre)+'\n'
        resp = resp +'\t Precio: ' + str(self.precio)+'\n'
        return resp
    
    def Captura(self):
        self.codigo = (input("Codigo: "))
        self.nombre = (input("Nombre: "))
        self.precio = float((input("Precio: ")))
        
        
class No_Original(Repuesto):
    def __init__(self, codigo=" " , nombre = " ", precio = 0.0, paisFabricacion= " " ):
        super().__init__( codigo, nombre, precio)
        self.__paisFabricacion = paisFabricacion
        

    @property
    def paisFabricacion(self):
        return self.__paisFabricacion

    @paisFabricacion.setter
    def paisFabricacion(self, paisFabricacion):
        self.__paisFabricacion = paisFabricacion
        

    def __str__(self):
            resp = super().__str__()
            resp += '\t Pais Fabricacion: ' + str(self.paisFabricacion) + ' \n'
            return resp
        
    def Captura(self):
        super().Captura()
        self.paisFabricacion = (input("Pais Fabricacion : "))
    def calculaPrecio(self):
        return 0
        
        
        
class Nuevo(Repuesto):
    def __init__(self,  codigo=" " , nombre = " ", precio = 0.0, annoGantia = 0 ):
        super().__init__( codigo, nombre, precio)
        self.__annoGantia = annoGantia
        

    @property
    def annoGantia(self):
        return self.__annoGantia

    @annoGantia.setter
    def annoGantia(self, annoGantia):
        self.__annoGantia = annoGantia
        

    def __str__(self):
            resp = super().__str__()
            resp += '\n \t Annos de Gantia: ' + str(self.annoGantia) + ' \n'
            resp += "\n--------------------------------------------------\n"
            return resp
        
    def Captura(self):
        super().Captura()
        self.annoGantia = int(input("Annos de Gantia : "))
        

from Fabricantes import Proveedor,  Fabricante_Original, Fabricante

from Fecha import Fecha, FechaTest


        
class Usados(No_Original):
    def __init__(self, codigo= " " , nombre = " ", precio = 0.0, paisFabricacion = " ",  fecha = Fecha(), fechaTest = FechaTest(), proveedor = [] ):
        super().__init__( codigo, nombre, precio, paisFabricacion)
        self.__proveedor = proveedor
        self.__fechaTest = fechaTest
        self.__fecha = fecha
        

    @property
    def proveedor(self):
        return self.__proveedor

    @proveedor.setter
    def proveedor(self, proveedor):
        self.__proveedor = proveedor
        
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
        
        
    @property
    def fechaTest(self):
        return self.__fechaTest

    @fechaTest.setter
    def fechaTest(self, fechaTest):
        self.__fechaTest = fechaTest

    def calculaPrecio(self):
        return self.precio + (0.10*self.precio )

    def __str__(self):
            resp =  ' ************************ Repuesto No Original Usado ************************ \n'
            resp += super().__str__()
            resp += '-------- Fecha de Fabricacion ---------- \n' + str(self.fecha)
            resp += '\t  ' + str(self.fechaTest)
            resp += '\t Precio a Pagar ' + str(self.calculaPrecio()) + ' \n'
            resp += "\n\n \t Proveedores: " 
            for i in range(len(self.proveedor)):
                resp += "\n"+ str(self.proveedor[i])
            resp += "\n--------------------------------------------------------\n"
            return resp
        
    def Captura(self):
        super().Captura()
        self.fecha.Captura()
        self.fechaTest.Captura()
        nump = int(input("Numero de Proveedores: "))
        for i in range(nump):
            prove = Proveedor()
            prove.Captura()
            self.proveedor.append(prove)
        

class Original(Nuevo):
    def __init__(self, codigo=" " , nombre = " ", precio = 0.0, annoGantia = 0,  fecha = Fecha(), fabricante_Original = Fabricante_Original() ):
        super().__init__( codigo, nombre, precio, annoGantia)
        self.__fabricante_Original = fabricante_Original
        self.__fecha = fecha
        

    @property
    def fabricante_Original(self):
        return self.__fabricante_Original

    @fabricante_Original.setter
    def fabricante_Original(self, fabricante_Original):
        self.__fabricante_Original = fabricante_Original
        
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
        

    def calculaPrecio(self):
        return self.precio + (0.25*self.precio )

    def __str__(self):
            resp =  ' ************************ Repuesto Nuevo Original ************************ \n'
            resp += super().__str__()
            resp += '-------- Fecha de Fabricacion ---------- \n' + str(self.fecha)
            resp += '\t  ' + str(self.fabricante_Original) + ' \n'
            resp += '\t Precio a Pagar ' + str(self.calculaPrecio()) + ' \n'
            resp += "\n--------------------------------------------------------\n"
            return resp
        
    def Captura(self):
        super().Captura()
        self.fecha.Captura()
        self.fabricante_Original.Captura()
        

 #   def __init__(self,  codigo=" " , nombre = " ", precio = 0.0, annoGantia = 0 ):
  #      def __init__(self, codigo=" " , nombre = " ", precio = 0.0, paisFabricacion= " " ):
            
class No_Nuevo(Nuevo,No_Original):
    def __init__(self, codigo=" " , nombre = " ", precio = 0.0, annoGantia = 0,paisFabricacion= " ", fabricante = Fabricante() ):
        Nuevo.__init__(self, codigo, nombre, precio, annoGantia)
        No_Original.__init__(self, codigo , nombre , precio , paisFabricacion)
        self.__fabricante = fabricante
        

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante
        
        

    def calculaPrecio(self):
        return self.precio + ((0.05*self.precio )*self.annoGantia)

    def __str__(self):
            resp =  ' ************************ Repuesto No Original Nuevo ************************ \n'
            resp += super().__str__()
            resp += "\n---------------Fabricante-------------------\n"
            resp += '  ' + str(self.fabricante) + ' \n'
            resp += '\t Precio a Pagar ' + str(self.calculaPrecio()) + ' \n'
            resp += "\n--------------------------------------------------------\n"
            return resp
        
    def Captura(self):
        super().Captura()
        self.fabricante.Captura()
        
        
        



"""        

fe = Fecha(10,11,2022)

feT = FechaTest(10,11,2022,10)

prov1 = Proveedor("Julio","CR","G4D14",75)
prov2 = Proveedor("Julio2","CR1","1G4D14",175)
fabO = Fabricante_Original("Julio","CR","San Jose","22564741","jul@gmail.com")
fab = Fabricante("Julio","CR")
prves = [prov1,prov2]
        
#re = Repuesto("F41A4","Bugia",450)
#reNO = No_Original("F41A4","Bugia",450,"Maldivas")
#usa = Usados("F41A4","Bugia",100,"Maldivas",fe,feT,prves)
#ori = Original("F41A4","Bugia",100,3,fe,fabO)
#nON = No_Nuevo("F41A4","Bugia",100,3,"CR",fab)
#reO = Nuevo("HOA1D","Motor",6000,4)
#nON.Captura()
#print(nON.__str__())

"""