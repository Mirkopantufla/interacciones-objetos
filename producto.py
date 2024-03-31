
class Producto():
    
    def __init__(self, nombre:str, precio:int, stock:int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def precio(self):
        return self.__precio
        
    @property
    def stock(self):
        return self.__stock
        
    @stock.setter
    def stock(self, stock_ingresado):
        self.__stock = stock_ingresado if stock_ingresado > 0 else 0

    def __add__(self, other):
        return self.stock + other.stock
        
    def __sub__(self, other):
        return self.stock - other.stock
        
    def __eq__(self, other):
        return self.nombre == other.nombre
    