from Repuesto import Usados,No_Nuevo, Original
import os


class Lectura():
    def LeeDatosUsados(self):
        usado = Usados()
        os.system('cls') 
        usado.Captura()
        return usado
    def LeeDatosNo_Nuevo(self):
        no_Nuevo = No_Nuevo()
        os.system('cls') 
        no_Nuevo.Captura()
        return no_Nuevo
    def LeeDatosOriginal(self):
        original = Original()
        os.system('cls')
        original.Captura()
        return original
    



