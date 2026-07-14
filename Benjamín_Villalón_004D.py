
recorridos = {
    'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
    'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
    'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
    'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
    'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
    'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True]
}

venta = {
    'R001': [7990, 20],
    'R002': [25990, 0],
    'R003': [1990, 35],
    'R004': [12990, 8],
    'R005': [18990, 3],
    'R006': [4990, 12]
}

def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("El valor debe ser mayor a 0.")
            else:
                return valor
        except Exception:
            print("Error; Debe ingresar únicamente números enteros.")

def solicitar_booleano(mensaje):
    while True:
        resp = input(mensaje).strip().lower()
        if resp in ["s", "si", "sí", "true"]:
            return True
        elif resp in ["n", "no", "false"]:
            return False
        else:
            print("Error; Debe responder 'S' para Sí y 'N' para No")

def validar_origen(mensaje):
    while True:
        valor = input(mensaje).lower()
        if len(valor) == 0:
            print("El valor no puede estar vacío.")
        elif len(valor) < 5:
            print("El valor debe contener como mínimo 5 carácteres.")
        else:
            return valor
        
def validar_tipo_bus(mensaje):
    while True:
        valor = input(mensaje).lower()
        if valor != "normal" and valor != "semi-cama" and valor != "cama":
            print("Debe ingresar una de las 3 opciones [normal/sami-cama/cama]")
        else:
            return valor
        
def validar_servicio(mensaje):
    while True:
        valor = input(mensaje).lower()
        if valor != "dia" and valor != "noche":
            print("Debe ingresar una de las 2 opciones [día/noche]")
        else:
            return valor
        
def validar_destino(mensaje):
    while True:
        valor = input(mensaje).lower()
        if len(valor) == 0:
            print("El valor no puede estar vacío.")
        elif len(valor) < 5:
            print("El valor debe contener como mínimo 5 carácteres.")
        else:
            return valor
        
def validar_codigo(mensaje):
    while True:
        valor = input(mensaje).upper()
        if len(valor) == 0:
            print("El código no puede estar vacío")
        else:
            return valor

def agregar_recorrido():
    codigo = validar_codigo("Ingrese el código del recorrido: ").strip().upper()
    if codigo in recorridos:
        print("Error; El código ya existe.")
        return
    
    origen = validar_origen("Ingrese origen: ").strip()
    destino = validar_destino("Ingrese destino: ").strip()
    distancia_km = solicitar_entero("Ingrese distancia: ")
    tipo_bus = validar_tipo_bus("Ingrese tipo de bus (normal/semi-cama/cama): ").strip()
    servicio = validar_servicio("Ingrese servicio (dia/noche): ").strip()
    tiene_wifi = solicitar_booleano("¿Tiene Wifi? (s/n): ")

    precio = solicitar_entero("Ingrese precio: ")
    asientos = solicitar_entero("Ingrese asientos: ")

    recorridos[codigo] = [origen,destino,distancia_km,tipo_bus,servicio,tiene_wifi]
    venta[codigo] = [precio,asientos]
    print(f"Recorrido agregado")

def eliminar_recorrido():
    codigo = input("Ingrese el código del recorrido a eliminar: ").strip().upper()
    if codigo in recorridos:
        eliminado = recorridos.pop(codigo)
        venta.pop(codigo,None)
        print(f"El recorrido {eliminado[0]} ha sido eliminado correctamente.")
    else:
        print("Error; No se puede borrar un código inexistente.")

def actualizar_precio_recorrido():
    codigo = input("Ingrese código del recorrido: ")
    if codigo not in recorridos:
        print("Error; El código no existe.")
        return
    precio_actual = venta[codigo][0] if codigo in venta else 0
    precio = solicitar_entero(F"Ingrese nuevo precio [{precio_actual}]: ")
    venta[codigo] = [precio]
    print("Precio actualizado correctamente")

def rango_precio():
    minimo = solicitar_entero("Ingrese precio mínimo: ")
    maximo = solicitar_entero("Ingrese precio máximo: ")
    if minimo > maximo:
        print("El precio mínimo no puede ser mayor al precio máximo.")
        return
    encontrados = False
    print(f"Recorridos entre ${minimo} y ${maximo}: ")
    for codigo, datos_venta in venta.items():
        precio = datos_venta[0]
        if minimo <= precio <= maximo:
            origen = recorridos[codigo][0] if codigo in recorridos else "Origen desconocido"
            destino = recorridos[codigo][1] if codigo in recorridos else "Destino desconocido"
            print(f"Los recorridos encontrados son: {origen}-{destino}--[{codigo}]")
            encontrados = True
    if not encontrados: 
        print("No se encontraron los recorridos en ese rango de precio.")

def buscar_recorridos():
    origen = validar_origen("Ingrese ciudad de origen a consultar: ")
    if origen in recorridos:
        datos = recorridos[origen]
        print(f"Origen: {datos}")
        if origen in venta:
            ven = venta[origen]
            print(f"Asientos: {ven[1]}")
        else:
            print("Error; El recorrido no tiene datos asociados en la venta.")
    else:
        print("El recorrido con ese origen no existe.")
    
def menu():
    while True:
        print("========= MENÚ PRINCIPAL =========")
        print("[1] Asientos por ciudad de origen.")
        print("[2] Búsqueda de recorridos por rango de precio.")
        print("[3] Actualizar precio de recorrido.")
        print("[4] Agregar recorrido.")
        print("[5] Eliminar recorrido.")
        print("[6] Salir")
        print("==================================")

        opcion = input("Elija una opción del [1 al 6]: ")

        if opcion == '1':
            buscar_recorridos()
        elif opcion == '2':
            rango_precio()
        elif opcion == '3':
            actualizar_precio_recorrido()
        elif opcion == '4':
            agregar_recorrido()
        elif opcion == '5':
            eliminar_recorrido()
        elif opcion == '6':
            print("Programa finalizado.")
            break
        else: 
            print("Debe seleccionar una opción válida [1 al 6].")  
menu()  