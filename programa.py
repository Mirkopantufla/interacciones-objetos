from tienda import TiendaRestaurante, TiendaFarmacia, TiendaSupermercado
import os

#Asigno valores de la tienda a lo ingresado por el usuario
nombre_tienda = input(f'''
Ingrese el nombre de la Tienda:
# > ''')
costo_delivery = input(f'''Ingrese el coste de delivery:
# > ''')

#Aca pruebo las tiendas creadas por tipo
tienda_seleccionada = TiendaRestaurante(nombre_tienda, costo_delivery)
# tienda_seleccionada = TiendaFarmacia(nombre_tienda, costo_delivery)
# tienda_seleccionada = TiendaSupermercado(nombre_tienda, costo_delivery)

condicion = True
#Primer loop para ingresar productos
while condicion:
    numero_opcion = input(f"""
Desea ingresar un nuevo producto?
1) si 
2) no
Ingrese el numero:
> """)
    numero_opcion = int(numero_opcion) if numero_opcion.isdigit() else numero_opcion
    #Opcion 1 ingresa productos
    if numero_opcion == 1:
        es_valido = False
        #Segundo loop para validar valores ingreados
        while es_valido == False:
            os.system("cls")
            nombre_producto = input(f'''
Ingrese el nombre del producto: 
> ''')
            precio_producto = input(f'''Ingrese el precio del producto: 
> ''')      
            stock_producto = input(f'''Ingrese el stock del producto
> ''')
            #Si precio y stock son digitos, procede a cambiar de formato y a guardar
            if precio_producto.isdigit() and stock_producto.isdigit():
                es_valido = True
                tienda_seleccionada.ingresar_producto(nombre_producto, int(precio_producto), int(stock_producto))
            else:
                print("Has ingresado un formato incorrecto, vuelve a intentarlo")
    #Opcion 2 continua ejecución
    elif numero_opcion == 2:
        #While para consultar acciones
        while condicion:
            opcion_interna = input(f"""
Ingrese el numero de opcion a escoger
1) Listar productos
2) Realizar una venta
3) Salir del programa
> """)
            opcion_interna = int(opcion_interna) if opcion_interna.isdigit() else opcion_interna
            #Opcion 1 listar productos
            if opcion_interna == 1:
                print(tienda_seleccionada.listar_productos())
            #Opcion 2 Realiza venta
            elif opcion_interna == 2:
                input_nombre_venta = input(f"""
Ingrese el nombre del producto a vender
> """)
                input_stock_venta = int(input(f"""Ingrese la cantidad a comprar
> """))         
                #Para mejor manejo de errores, se asigna mensaje y si es valido para especificar donde fallo el ingreso
                venta_valida, mensaje = tienda_seleccionada.realizar_venta(input_nombre_venta, input_stock_venta)
                if not venta_valida:
                    print(mensaje)
                else:
                    print(f"Muchas gracias por comprar en {tienda_seleccionada.tipo} {tienda_seleccionada.nombre}")
            #Opcion 2 Termina toda la ejecucion
            elif opcion_interna == 3:
                print("Muchas gracias por utilizar nuestro software.")
                condicion = False
            else:
                os.system("cls")
                print("Opcion incorrecta, debe ser 1, 2 o 3")
    #En caso de que el primer loop haya sido ingresado mal, enviara mensaje para continuar ejecucion
    else:
        os.system("cls")
        print("Opcion incorrecta, debe ser 1 o 2")