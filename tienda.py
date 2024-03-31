from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):

    @abstractmethod
    def ingresar_producto(self, nombre, precio, stock):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass


#------------------------------------------ RESTAURANTE ------------------------------------------
class TiendaRestaurante(Tienda):
    tipo = "Restaurante"

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__listado_productos = []
        self.__costo_delivery = costo_delivery

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    @property
    def costo_delivery(self):
        return self.__costo_delivery

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        nuevo_producto = Producto(nombre, precio, 0)
        self.listado_productos.append(nuevo_producto)

    def listar_productos(self):
        if len(self.listado_productos) > 0:
            print_lista_productos = ""
            for producto in self.listado_productos:
                print_lista_productos += f'''Nombre: {producto.nombre}\t\tPrecio: {producto.precio}\n'''
            return print_lista_productos
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        mensaje = ""
        return True, mensaje


        
#------------------------------------------ SUPERMERCADO ------------------------------------------
class TiendaSupermercado(Tienda):
    tipo = "Supermercado"

    def __init__(self, nombre:str, costo_delivery:int):
        self.__nombre = nombre
        self.__listado_productos = []
        self.__costo_delivery = costo_delivery

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    @property
    def costo_delivery(self):
        return self.__costo_delivery

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        nuevo_producto = Producto(nombre, precio, stock)
        exist = nuevo_producto in self.__listado_productos

        if exist:
            index = self.__listado_productos.index(nuevo_producto)
            self.__listado_productos[index].stock = nuevo_producto + self.__listado_productos[index]
        else:
            self.__listado_productos.append(nuevo_producto)

    def listar_productos(self):

        if len(self.__listado_productos) > 0:
            print_lista_productos = ""
            for producto in self.__listado_productos:
                advertencia = "¡Pocos productos disponibles!" if producto.stock < 10 else ""
                print_lista_productos += f'''Nombre: {producto.nombre}\t\tPrecio: {producto.precio}\t\tStock: {producto.stock} {advertencia}\n'''
            return print_lista_productos
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto:str, cantidad_requerida:int):
        mensaje = ""
    # Las tiendas de tipo Farmacia y Supermercado deben tener
    # Stock existente del producto indicado (si no poseen stock, o no existe el producto
    # Solicitado, no se realiza ninguna acción).
        for producto in self.__listado_productos:
            index = self.__listado_productos.index(producto)

            # Si el producto existe
            if producto.nombre == nombre_producto:
                # Si hay stock disponible
                if producto.stock >= cantidad_requerida:
                    self.__listado_productos[index].stock = producto.stock - cantidad_requerida

                if cantidad_requerida > producto.stock:
                    self.__listado_productos[index].stock = 0
            else:
                mensaje = "Error: El producto es inexistente"
                return False, mensaje
            
        return True, mensaje

#------------------------------------------ FARMACIA ------------------------------------------
class TiendaFarmacia(Tienda):
    tipo = "Farmacia"

    def __init__(self, nombre:str, costo_delivery:int):
        self.__nombre = nombre
        self.__listado_productos = []
        self.__costo_delivery = costo_delivery

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    @property
    def costo_delivery(self):
        return self.__costo_delivery

    def ingresar_producto(self, nombre:str, precio:int, stock:int):
        nuevo_producto = Producto(nombre, precio, stock)
        exist = nuevo_producto in self.__listado_productos

        if exist:
            index = self.__listado_productos.index(nuevo_producto)
            self.__listado_productos[index].stock = nuevo_producto + self.__listado_productos[index]
        else:
            self.__listado_productos.append(nuevo_producto)
    
    def listar_productos(self):

        if len(self.__listado_productos) > 0:
            print_lista_productos = ""
            for producto in self.__listado_productos:
                promocion = "Envío gratis al solicitar este producto" if producto.precio > 15000 else ""
                print_lista_productos += f'''Nombre: {producto.nombre}\tPrecio: {producto.precio} {promocion}\n'''
            return print_lista_productos
        else:
            return "No hay productos en la Farmacia"
        
    def realizar_venta(self, nombre_producto:str, cantidad_requerida:int):
        mensaje = ""
        # Las tiendas de tipo Farmacia y Supermercado deben tener
        # stock existente del producto indicado (si no poseen stock, o no existe el producto
        # solicitado, no se realiza ninguna acción).
        for producto in self.__listado_productos:
            
            index = self.__listado_productos.index(producto)
            #Si el producto existe y si hay stock disponible
            if cantidad_requerida <= 3:
                if producto.nombre == nombre_producto:
                    if producto.stock > cantidad_requerida:
                        self.__listado_productos[index].stock = producto.stock - cantidad_requerida
                    elif cantidad_requerida > producto.stock:
                        self.__listado_productos[index].stock = 0
                else:
                    mensaje = "Error: El producto es inexistente"
                    return False, mensaje
            else:
                mensaje = "Error: Debes comprar menos de 3"
                return False, mensaje
            
        return True, mensaje