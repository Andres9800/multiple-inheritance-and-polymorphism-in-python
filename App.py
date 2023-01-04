from Lectura import Lectura
import os

class App:
    def __init__(self):
        self.__lista = list()
        self.__lec = Lectura()
    def __menu(self):
        #os.system('clear') #os.system('cls') #en windows
        print(" ==================================================== ")
        print(" [1] Insertar Repuesto No Original Usado")
        print(" [2] Insertar Repuesto No Original Nuevo ")
        print(" [3] Insertar Repuesto Original Nuevo ")
        print(" [4] Ver la lista de Repuestos" )
        print(" [5] Borrar la lista de Repuestos")
        print(" [6] Salir")
        print(" ==================================================== ")
        return input("> ")
    
    def __mostrarLista(self):
        os.system ("cls") 
        for i in range(len(self.__lista)):
            print(self.__lista[i])
          

    def principal(self):
        respuesta = ""
        while respuesta != "6":
            respuesta = self.__menu()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosUsados())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosNo_Nuevo())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatosOriginal())
            elif respuesta == "4":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar")
            elif respuesta == "5":
                self.__lista.clear()

prueba = App()
prueba.principal()


