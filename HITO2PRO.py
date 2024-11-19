'''● Registro de cliente: se pedirán sus datos personales. Cada cliente debe tener un
campo único.
● Visualizar todos los clientes registrados y realizar búsquedas de clientes a través de
su campo único.
● Realizar una compra: cada compra estará asociada a un cliente y puede tener uno o
varios productos. Los artículos estarán cargados previamente en la aplicación. Al
finalizar cada compra se mostrará el número del pedido.
● Seguimiento de una compra: mediante el número de pedido se mostrarán todos los
datos del cliente y del pedido.
'''
id_pedido = 1
registro_cliente = []
numero_pedido = ""
clientes = {}
productos = ['Manzana', 'pera', 'platano', 'naranja', 'limon', 'cookies', 'helados', 'bollos']
#Creamos una funcion para registrar el cliente que pida el nombre el dni y le preguntamos si quiere seguir registrando clientes 
def registrar_cliente():
    parar_registro = False
    while not parar_registro:
        nombre = input("Ingresa tu nombre: ")
        dni = input("Ingresa tu dni: ")
        print("El usuario con nombre " + nombre + " y dni " + dni + " ha sido registrado correctamente, ¿Deseas seguir registrando clientes?: ")
        respuesta_valida = False
        while not respuesta_valida:
            respuesta = input("SI/NO: ")
            if respuesta.lower() == "no":
                parar_registro = True
                respuesta_valida = True
            elif respuesta.lower() == "si":
                respuesta_valida = True
            else:
                print("Respuesta no válida, ingrese SI o NO")
        clientes[dni] = {"nombre": nombre, "compras": []}
#creamos una funcion para que pida el dni para visualizar al cliente
def visualizar_clientes():
    print("Escribe el dni del cliente que quieres visualizar")
    dni_cliente = input()
    print(clientes[dni_cliente])
#Creamos una funcion para realizar una compra en la que se pide el dni al comprador y se le muestran los productos que tiene para comprar  luego se le asignan un numero de pedido
def realizar_compra():
    global id_pedido
    comprador = input("Introduce tu dni: ")
    if comprador not in clientes:
        print("El cliente no está registrado.")
        return
    print("Estos son los productos disponibles para comprar:", productos)
    lista_productos = []
    compra = ""
    while compra != "salir":
        compra = input("Selecciona un producto o escribe 'salir' para finalizar: ").lower()
        if compra != "salir":
            if compra in [producto.lower() for producto in productos]:
                lista_productos.append(compra)
            else:
                print("Producto no válido, intenta de nuevo.")

    if lista_productos:
        pedido = {"id_compra": id_pedido, "productos": lista_productos}
        clientes[comprador]["compras"].append(pedido)
        print(f"Compra realizada con éxito. Número de pedido: {id_pedido}")
        id_pedido += 1
    else:
        print("No se ha seleccionado ningún producto.")
#Funcion para realizar el seguimiento de la compra introduciendo el numero de pedido 
def seguimiento_compra():
    numero_pedido = input("Introduce el número de pedido para realizar el seguimiento: ")
    for cliente in clientes.values():
        for compra in cliente["compras"]:
            if str(compra["id_compra"]) == numero_pedido:
                print(f"Cliente: {cliente['nombre']}, Pedido: {compra}")
                return
    print("Pedido no encontrado.")
#este es el menu en el que llamaremos a las funciones anteriores para realizarlas
def mostrar_menu():
    while True:
        print("Que desea hacer 1:Registrar cliente, 2: Mostrar clientes, 3: Realizar compras, 4: Seguimiento de la compra, 5: Salir ")
        respuesta = input("Selecciona un número: ")
        if respuesta == "1":
            registrar_cliente()
        elif respuesta == "2":
            visualizar_clientes()
        elif respuesta == "3":
            realizar_compra()
        elif respuesta == "4":
            seguimiento_compra()
        elif respuesta == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

mostrar_menu()