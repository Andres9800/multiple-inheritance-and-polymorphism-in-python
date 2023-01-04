# -*- coding: utf-8 -*-
from Base import Base

class Fecha(Base):
    def __init__(self, dia=0 , mes = 0, anno = 0):
        self.__dia = dia
        self.__mes = mes
        self.__anno = anno
    
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia
        
    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def anno(self):
        return self.__anno
    
    @anno.setter
    def anno(self, anno):
        self.__anno = anno
   
    def __str__(self):
        
        resp = '\t Dia: ' + str(self.dia) + '\n'
        resp = resp +'\t Mes: ' + str(self.mes)+'\n'
        resp = resp +'\t Anno: ' + str(self.anno)+'\n'
        return resp
    
    def Captura(self):
        self.dia = int(input("Dia : "))
        self.mes = int(input("Mes: "))
        self.anno = int(input("Anno: "))
        
        
class FechaTest(Fecha):
    def __init__(self,  dia=0 , mes = 0, anno = 0, numeroDias = 0 ):
        super().__init__( dia, mes, anno)
        self.__numeroDias = numeroDias

    @property
    def numeroDias(self):
        return self.__numeroDias

    @numeroDias.setter
    def numeroDias(self, numeroDias):
        self.__numeroDias = numeroDias
    
    def __str__(self):
            resp = "\n------------Fecha Test------------\n"
            resp += super().__str__()
            resp += '\n \t Plazo de Garantia: ' + str(self.numeroDias)
            return resp
        
    def Captura(self):
        super().Captura()
        self.numeroDias = int(input("Periodo de garantia: "))

    
    


"""

fe = Fecha(10,11,2022)

feT = FechaTest(10,11,2022,10)
feT.Captura()
#feN = fe.Captura()

print(feT.__str__())
        
""" 