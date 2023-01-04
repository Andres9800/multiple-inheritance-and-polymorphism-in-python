# -*- coding: utf-8 -*-
from abc import  ABCMeta, abstractmethod

class Base(metaclass = ABCMeta):    
    @abstractmethod
    def __str__(self):
        pass    
    @abstractmethod
    def Captura(self):
        pass 