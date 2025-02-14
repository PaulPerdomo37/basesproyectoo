import mysql.connector
from datetime import datetime  # Importación corregida

def conectar_db():
    """Conecta a la base de datos MySQL usando XAMPP."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Usuario por defecto en XAMPP
            password="Elementales11",  # Sin contraseña por defecto en XAMPP
            database="sistemaempleados"  # Nombre correcto de la base de datos
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def agregar_empleado(nombre, usuario, contrasena, horario):
    """Agrega un empleado utilizando el procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.callproc("sp_insert_empleado", (nombre, usuario, contrasena, horario))
            conexion.commit()
            print("Empleado agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar empleado: {err}")
        finally:
            cursor.close()
            conexion.close()
def editar_empleado(id_empleado, nombre, usuario, contrasena, horario):
    """Edita un empleado utilizando el procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "CALL sp_update_empleado(%s, %s, %s, %s, %s)",
                (id_empleado, nombre, usuario, contrasena, horario)
            )
            conexion.commit()
            print("Empleado editado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al editar empleado: {err}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_empleado(id_empleado):
    """Elimina un empleado utilizando el procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.callproc("sp_delete_empleado", (id_empleado,))
            conexion.commit()
            print("Empleado eliminado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar empleado: {err}")
        finally:
            cursor.close()
            conexion.close()

def listar_empleados():
    """Lista todos los empleados de la base de datos."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT * FROM Empleado"
            cursor.execute(query)
            empleados = cursor.fetchall()

            print("Lista de empleados:")
            for empleado in empleados:
                print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Usuario: {empleado[2]}, Horario: {empleado[4]}")
        except mysql.connector.Error as err:
            print(f"Error al listar empleados: {err}")
        finally:
            cursor.close()
            conexion.close()
def eliminarHijos(id_empleado, tabla):
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            query_eliminar = f"DELETE FROM {tabla} WHERE id_empleado = %s"
            cursor.execute(query_eliminar, (id_empleado,))
            conexion.commit()

            if cursor.rowcount > 0:
                
                return True
            else:
              return False  
        except mysql.connector.Error as err:
            print(f"Error al eliminar usuario: {err}")
            
        finally:
            cursor.close()
            conexion.close() 
        


def eliminar_usuario_tipo2(id_empleado, tipo_usuario):
    """Elimina un empleado de una tabla específica (tipo de usuario)."""
    conexion = conectar_db()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        tablas = {
            "administrador": "administradorgeneral",
            "soporte": "soportecliente",
            "vendedor": "vendedor",
            "marketing": "especialistamarketing",
            "inventario": "encargadoinventario",
        }
        tabla = tablas.get(tipo_usuario.lower())

        if not tabla:
            print("Tipo de usuario no válido.")
            return False

        
        if tabla == "encargadoinventario":
            eliminarHijos(id_empleado, "gestion")
        elif tabla == "vendedor":
            query = "SELECT ID_Venta FROM venta WHERE ID_Empleado = %s"
            cursor.execute(query, (id_empleado,))
            ventas = cursor.fetchall()
            for venta in ventas:
                eliminarHijos(venta[0], "venta")
            eliminarHijos(id_empleado, "registroventa")
        elif tabla == "especialistamarketing":
            eliminarHijos(id_empleado, "gestionoferta")

        # Eliminar el empleado
        query_eliminar = f"DELETE FROM {tabla} WHERE ID_Empleado = %s"
        cursor.execute(query_eliminar, (id_empleado,))
        conexion.commit()

        if cursor.rowcount > 0:
            print(f"Empleado eliminado exitosamente de {tabla}.")
            return True
        else:
            print("Empleado no encontrado.")
            return False

    except mysql.connector.Error as err:
        print(f"Error al eliminar usuario: {err}")
        return False

    except Exception as e:
        print(f"Error inesperado: {e}")
        return False

    finally:
        cursor.close()
        conexion.close()




def validar_usuario(tabla, usuario, contrasena):
    """Valida el usuario y contraseña en la tabla correspondiente y devuelve el ID del empleado."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = f"SELECT ID_Empleado FROM {tabla} WHERE Usuario = %s AND Contraseña = %s"
            cursor.execute(query, (usuario, contrasena))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None  # Devuelve el ID si el usuario existe
        except mysql.connector.Error as err:
            print(f"Error al validar usuario: {err}")
            return None
        finally:
            cursor.close()
            conexion.close()
#Editar empleado

    
# Menú de la aplicación
def agendar_usuario(id_empleado, tipo_usuario):
    """Asigna un empleado a una tabla específica (tipo de usuario)."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query_buscar = "SELECT * FROM Empleado WHERE ID_Empleado = %s"
            cursor.execute(query_buscar, (id_empleado,))
            empleado = cursor.fetchone()

            if not empleado:
                print("No se encontró un empleado con ese ID.")
                return

            tabla = {
                "administrador": "administradorgeneral",
                "soporte": "soportecliente",
                "vendedor": "vendedor",
                "marketing": "especialistamarketing",
                "inventario": "encargadoinventario"
            }.get(tipo_usuario.lower())

            if not tabla:
                print("Tipo de usuario no válido.")
                return

            query_insertar = (
                f"INSERT INTO {tabla} (ID_Empleado, Nombre, Usuario, Contrase\u00f1a, Horario) "
                "VALUES (%s, %s, %s, %s, %s)"
            )
            valores = (empleado[0], empleado[1], empleado[2], empleado[3], empleado[4])
            cursor.execute(query_insertar, valores)
            conexion.commit()
            print(f"Empleado agendado exitosamente en {tabla}.")
        except mysql.connector.Error as err:
            print(f"Error al agendar usuario: {err}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_usuario_tipo(id_empleado, tipo_usuario):
    """Elimina un empleado de una tabla específica (tipo de usuario)."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            tabla = {
                "administrador": "administradorgeneral",
                "soporte": "soportecliente",
                "vendedor": "vendedor",
                "marketing": "especialistamarketing",
                "inventario": "encargadoinventario"
            }.get(tipo_usuario.lower())

            if not tabla:
                print("Tipo de usuario no válido.")
                return

            query_eliminar = f"DELETE FROM {tabla} WHERE ID_Empleado = %s"
            cursor.execute(query_eliminar, (id_empleado,))
            conexion.commit()

            if cursor.rowcount > 0:
                print(f"Empleado eliminado exitosamente de {tabla}.")
            else:
                print("No se encontró un empleado con ese ID en la tabla especificada.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar usuario: {err}")
        finally:
            cursor.close()
            conexion.close()
def gestionar_registros():
    """Permite gestionar registros de las tablas especificadas."""
    while True:
        print("\n=== Gestión de Registros ===")
        print("1. Registros de gestión")
        print("2. Registros de gestión de oferta")
        print("3. Registros de promociona")
        print("4. Registros de registro de venta")
        print("5. Volver al menú anterior")

        opcion_tabla = input("Selecciona una opción: ")

        if opcion_tabla == "1":
            tabla = "gestion"
            claves_primarias = ["id_gestion"]  # Clave primaria única
        elif opcion_tabla == "2":
            tabla = "gestionoferta"
            claves_primarias = ["id_empleado", "id_oferta"]  # Clave compuesta
        elif opcion_tabla == "3":
            tabla = "promociona"
            claves_primarias = ["id_oferta", "id_redsocial"]  # Clave compuesta
        elif opcion_tabla == "4":
            tabla = "registroventa"
            claves_primarias = ["id_venta", "sku_producto"]  # Clave compuesta
        elif opcion_tabla == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue

        while True:
            print(f"\n=== Opciones para la tabla {tabla} ===")
            print("1. Ver registros")
            print("2. Editar registro")
            print("3. Eliminar registro")
            print("4. Volver al menú anterior")

            opcion_accion = input("Selecciona una acción: ")

            if opcion_accion == "1":
                mostrar_tabla(tabla)
            elif opcion_accion == "2":
                editar_registro_compuesto(tabla, claves_primarias)
            elif opcion_accion == "3":
                eliminar_registro_compuesto(tabla, claves_primarias)
            elif opcion_accion == "4":
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

def mostrar_tabla(tabla):
    """Muestra todos los registros de una tabla."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = f"SELECT * FROM {tabla}"
            cursor.execute(query)
            registros = cursor.fetchall()
            print(f"\n=== Registros en la tabla {tabla} ===")
            for registro in registros:
                print(registro)
        except mysql.connector.Error as err:
            print(f"Error al mostrar registros: {err}")
        finally:
            cursor.close()
            conexion.close()

def editar_registro_compuesto(tabla, claves_primarias):
    """Edita un registro en la tabla especificada con claves compuestas."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            condiciones = {}
            for clave in claves_primarias:
                valor = input(f"Introduce el valor para {clave}: ")
                condiciones[clave] = valor

            campo = input("Introduce el campo a modificar: ")
            nuevo_valor = input("Introduce el nuevo valor: ")

            where_clause = " AND ".join([f"{clave} = %s" for clave in condiciones.keys()])
            query = f"UPDATE {tabla} SET {campo} = %s WHERE {where_clause}"
            cursor.execute(query, [nuevo_valor] + list(condiciones.values()))
            conexion.commit()

            if cursor.rowcount > 0:
                print("Registro actualizado exitosamente.")
            else:
                print("No se encontró el registro con los valores proporcionados.")
        except mysql.connector.Error as err:
            print(f"Error al editar el registro: {err}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_registro_compuesto(tabla, claves_primarias):
    """Elimina un registro de la tabla especificada con claves compuestas."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            condiciones = {}
            for clave in claves_primarias:
                valor = input(f"Introduce el valor para {clave}: ")
                condiciones[clave] = valor

            where_clause = " AND ".join([f"{clave} = %s" for clave in condiciones.keys()])
            query = f"DELETE FROM {tabla} WHERE {where_clause}"
            cursor.execute(query, list(condiciones.values()))
            conexion.commit()

            if cursor.rowcount > 0:
                print("Registro eliminado exitosamente.")
            else:
                print("No se encontró el registro con los valores proporcionados.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar el registro: {err}")
        finally:
            cursor.close()
            conexion.close()
def menu_administrador():
    """Muestra el menú de administrador."""
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Eliminar empleado")
        print("4. editar empleado")
        print("5. Agendar empleado en tipo de usuario")
        print("6. Eliminar empleado de tipo de usuario")
        print("7. Registros")
        print("8. Volver al menu principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            horario = input("Horario (ej. 08:00-17:00): ")
            agregar_empleado(nombre, usuario, contrasena, horario)
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            id_empleado = int(input("ID del empleado a eliminar: "))
            eliminar_empleado(id_empleado)
        elif opcion == "4":
            id_empleado = int(input("ID del empleado a editar: "))
            Nombre = input("nuevo nombre: ")
            Usuario = input ("Ingrese nuevo Usuario: ")
            contraseña = input("ingrese nueva contraseña: ")
            horario = input("ingrese nuevo Horario (ej. 08:00-17:00): ")
            editar_empleado(id_empleado,Nombre,Usuario,contraseña,horario)
        elif opcion == "5":
            id_empleado = int(input("ID del empleado a agendar: "))
            tipo_usuario = input("Tipo de usuario (administrador, soporte, vendedor, marketing, inventario): ")
            agendar_usuario(id_empleado, tipo_usuario)
        elif opcion == "6":
            id_empleado = int(input("ID del empleado a eliminar: "))
            tipo_usuario = input("Tipo de usuario (administrador, soporte, vendedor, marketing, inventario): ")
            eliminar_usuario_tipo(id_empleado, tipo_usuario)
        elif opcion == "7":
            gestionar_registros()
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def obtener_producto(id_producto):
    """Obtiene un producto de la base de datos por su ID."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT * FROM producto WHERE sku = %s"
            cursor.execute(query, (id_producto,))
            producto = cursor.fetchone()
            return producto
        except mysql.connector.Error as err:
            print(f"Error al obtener producto: {err}")
            return None
        finally:
            cursor.close()
            conexion.close()

def actualizar_producto(id_producto, campo, nuevo_valor):
    """Actualiza un campo específico de un producto utilizando un procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "CALL sp_update_producto(%s, %s, %s)",
                (id_producto, campo, nuevo_valor)
            )
            conexion.commit()
            print(f"El campo '{campo}' se actualizó correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar producto: {err}")
        finally:
            cursor.close()
            conexion.close()

def registrar_gestion(id_empleado, id_producto, descripcion):
    """Registra un cambio en la tabla de gestión."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual
            query = (
                "INSERT INTO gestion (id_empleado, sku, descripcion, fecha) "
                "VALUES (%s, %s, %s, %s)"
            )
            valores = (id_empleado, id_producto, descripcion, fecha_actual)
            cursor.execute(query, valores)
            conexion.commit()
            print("Gestión registrada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al registrar gestión: {err}")
        finally:
            cursor.close()
            conexion.close()

def menu_encargado_inventario(id_empleado):
    """Muestra el menú del encargado de inventario."""

    while True:
        print("\n=== Menú Encargado de Inventario ===")
        print("1. Editar un producto")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("Introduce el SKU del producto a editar: ")
            producto = obtener_producto(id_producto)

            if not producto:
                print("No se encontró un producto con ese SKU.")
                continue

            print("\n=== Datos del Producto ===")
            print(f"SKU: {producto[0]}\nCategoría: {producto[1]}\nNombre: {producto[2]}\nPrecio: {producto[3]}\nID Proveedor: {producto[4]}\nStock: {producto[5]}")

            descripcion_cambios = []

            while True:
                print("\n=== Opciones de Edición ===")
                print("1. Editar Categoría")
                print("2. Editar Nombre")
                print("3. Editar Precio")
                print("4. Editar ID Proveedor")
                print("5. Editar Stock")
                print("6. Salir de Edición")

                opcion_editar = input("Selecciona una opción para editar: ")

                if opcion_editar == "1":
                    nuevo_valor = input("Nueva Categoría: ")
                    actualizar_producto(id_producto, "categoria", nuevo_valor)
                    descripcion_cambios.append("Categoría actualizada")
                elif opcion_editar == "2":
                    nuevo_valor = input("Nuevo Nombre: ")
                    actualizar_producto(id_producto, "nombre", nuevo_valor)
                    descripcion_cambios.append("Nombre actualizado")
                elif opcion_editar == "3":
                    nuevo_valor = input("Nuevo Precio: ")
                    try:
                        nuevo_valor = float(nuevo_valor)
                        actualizar_producto(id_producto, "precio", nuevo_valor)
                        descripcion_cambios.append("Precio actualizado")
                    except ValueError:
                        print("El precio debe ser un número válido.")
                elif opcion_editar == "4":
                    nuevo_valor = input("Nuevo ID Proveedor: ")
                    actualizar_producto(id_producto, "id_proveedor", nuevo_valor)
                    descripcion_cambios.append("ID Proveedor actualizado")
                elif opcion_editar == "5":
                    nuevo_valor = input("Nuevo Stock: ")
                    try:
                        nuevo_valor = int(nuevo_valor)
                        actualizar_producto(id_producto, "stock", nuevo_valor)
                        descripcion_cambios.append("Stock actualizado")
                    except ValueError:
                        print("El stock debe ser un número entero.")
                elif opcion_editar == "6":
                    if descripcion_cambios:
                        descripcion = ", ".join(descripcion_cambios)
                        registrar_gestion(id_empleado, id_producto, descripcion)
                    print("Saliendo de edición.")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

        elif opcion == "2":
            print("Saliendo del menú de inventario.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")






           
def obtener_clientes_necesitan_ayuda(id_empleado):
    """Obtiene la lista de clientes que necesitan ayuda utilizando el procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("CALL sp_obtener_clientes_necesitan_ayuda(%s)", (id_empleado,))
            clientes = cursor.fetchall()
            return clientes
        except mysql.connector.Error as err:
            print(f"Error al obtener clientes: {err}")
            return None
        finally:
            cursor.close()
            conexion.close()

def eliminar_venta_cliente(id_cliente):
    """Elimina la venta asociada a un cliente utilizando el procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Obtener las ventas asociadas al cliente
            query = "SELECT ID_Venta, Fecha FROM venta WHERE ID_Cliente = %s"
            cursor.execute(query, (id_cliente,))
            ventas = cursor.fetchall()

            if not ventas:
                print(f"No se encontraron ventas asociadas al cliente con ID {id_cliente}.")
                return

            # Mostrar las ventas y permitir al usuario seleccionar una
            for venta in ventas:
                print(f"ID_Venta = {venta[0]}, Fecha = {venta[1]}")

            id_v = input("\nSelecciona el ID de la venta que desea eliminar: ")

            # Llamar al procedimiento almacenado para eliminar la venta
            cursor.execute("CALL sp_eliminar_venta_cliente(%s, %s)", (id_cliente, id_v))
            conexion.commit()

            if cursor.rowcount > 0:
                print(f"Venta del cliente con ID {id_cliente} eliminada exitosamente.")
            else:
                print(f"No se encontró una venta asociada al cliente con ID {id_cliente}.")

        except mysql.connector.Error as err:
            print(f"Error al eliminar venta: {err}")
        finally:
            cursor.close()
            conexion.close()

def menu_soporte_cliente(id_empleado):
    """Muestra el menú de soporte al cliente."""
    
    while True:
        print("\n=== Menú Soporte al Cliente ===")
        print("1. Elegir usuario para dar soporte")
        print("2. Salir")

        opcion_editar = input("Selecciona una opción: ")
        
        if opcion_editar == "1":
            
            clientes = obtener_clientes_necesitan_ayuda(id_empleado)
            if clientes:
                print("\n=== Clientes que necesitan ayuda ===")
                for cliente in clientes:
                    print(f"ID Cliente: {cliente[0]}, Nombre: {cliente[1]}")
                
                
                id_cliente = input("\nSelecciona el ID del cliente para dar soporte: ")
                try:
                    id_cliente = int(id_cliente)
                    eliminar_venta_cliente(id_cliente) 
                except ValueError:
                    print("Por favor, introduce un ID válido.")
            else:
                print("No hay clientes que necesiten ayuda en este momento.")

        elif opcion_editar == "2":
            print("Saliendo del menú de soporte al cliente.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
def ver_ofertas(id_empleado):
        conexion = conectar_db()
        cursor = conexion.cursor()
        query = """
                        SELECT *
                        FROM oferta o
                        
                    """  
        cursor.execute(query)
        ofertas = cursor.fetchall()
        if ofertas:
            print("\n=== Ofertas Actuales ===")
            for oferta in ofertas:
                print(f"ID: {oferta[0]}, Fecha Inicio: {oferta[1]}, Fecha Final: {oferta[2]}, SKU: {oferta[3]}, Descripción: {oferta[4]}, Descuento: {oferta[5]}%")
        else:
            print("No hay ofertas registradas.")

def agregar_oferta(id_empleado):
    """Agrega una nueva oferta utilizando el procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            id_oferta = input("Ingrese la id_oferta: ")
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_final = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")
            sku = input("Ingrese el SKU del producto: ")
            descripcion = input("Ingrese la descripción de la oferta: ")
            porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
            
            cursor = conexion.cursor()
            cursor.execute(
                "CALL sp_agregar_oferta(%s, %s, %s, %s, %s, %s, %s)",
                (id_empleado, id_oferta, fecha_inicio, fecha_final, sku, descripcion, porcentaje_descuento)
            )
            conexion.commit()
            print("Oferta agregada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar oferta: {err}")
        finally:
            cursor.close()
            conexion.close()


def actualizar_oferta():
    """Actualiza una oferta utilizando el procedimiento almacenado."""
    conexion = conectar_db()
    if conexion:
        try:
            id_oferta = int(input("Ingrese el ID de la oferta a actualizar: "))
            nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
            nueva_fecha_final = input("Ingrese la nueva fecha de finalización (YYYY-MM-DD): ")
            nuevo_sku = input("Ingrese el nuevo SKU del producto: ")
            nueva_descripcion = input("Ingrese la nueva descripción de la oferta: ")
            nuevo_porcentaje_descuento = float(input("Ingrese el nuevo porcentaje de descuento: "))
            
            cursor = conexion.cursor()
            cursor.execute(
                "CALL sp_actualizar_oferta(%s, %s, %s, %s, %s, %s)",
                (id_oferta, nueva_fecha_inicio, nueva_fecha_final, nuevo_sku, nueva_descripcion, nuevo_porcentaje_descuento)
            )
            conexion.commit()
            print("Oferta actualizada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar oferta: {err}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_oferta():
    """Elimina una oferta utilizando el procedimiento almacenado con validaciones."""
    conexion = conectar_db()
    if conexion:
        try:
            id_oferta = int(input("Ingrese el ID de la oferta a eliminar: "))
            
            cursor = conexion.cursor()
            cursor.execute("CALL sp_eliminar_oferta(%s)", (id_oferta,))
            
            # Mostrar el mensaje devuelto por el procedimiento almacenado
            resultado = cursor.fetchall()
            for mensaje in resultado:
                print(mensaje[0])
                
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error al eliminar oferta: {err}")
        finally:
            cursor.close()
            conexion.close()


def menu_especialista_marketing(id_empleado):
    """Muestra el menú del especialista en marketing."""
    while True:
        print("\n=== Menú Especialista en Marketing ===")
        print("1. ver ofertas ")
        print("2. agregar ofertas")
        print("3. actualizar ofertas")
        print("4. eliminar ofertas")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            ver_ofertas(id_empleado)
        elif opcion == "2":
            agregar_oferta(id_empleado)
        elif opcion == "3":
            actualizar_oferta()
        elif opcion == "4":
             eliminar_oferta()
        elif opcion == "5":
            print("Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")     

def registrar_venta(conn, id_empleado):
    cursor = conn.cursor()
    print("Ingrese el ID del cliente:")
    id_cliente = int(input())

    # Insertar nueva venta
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual
    query = "INSERT INTO venta (id_cliente, id_empleado, fecha, total) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id_cliente, id_empleado, fecha_actual, 0))
    id_venta = cursor.lastrowid
    print(f"Venta creada con ID: {id_venta} y fecha: {fecha_actual}")
    conn.commit()

    total_venta = 0

    # Menú de agregar/eliminar productos
    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Salir y registrar venta")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingrese el SKU del producto:")
            sku = input()

            # Obtener precio del producto
            cursor.execute("SELECT precio FROM producto WHERE sku = %s", (sku,))
            resultado = cursor.fetchone()

            if resultado:
                precio = resultado[0]
                total_venta += precio

                # Insertar en registroventa
                cursor.execute("INSERT INTO registroventa (id_venta, sku_producto, fecha) VALUES (%s, %s, %s)",
                               (id_venta, sku, fecha_actual))
                print(f"Producto {sku} agregado con precio {precio}. Total actual: {total_venta}")
            else:
                print("Producto no encontrado.")

        elif opcion == "2":
            print("Ingrese el SKU del producto a eliminar:")
            sku = input()

            # Buscar si el producto existe en registroventa
            cursor.execute("SELECT * FROM registroventa WHERE id_venta = %s AND sku_producto = %s LIMIT 1",
                           (id_venta, sku))
            registro = cursor.fetchone()

            if registro:
                # Obtener precio del producto
                cursor.execute("SELECT precio FROM producto WHERE sku = %s", (sku,))
                precio = cursor.fetchone()[0]
                total_venta -= precio

                # Eliminar producto del registroventa
                cursor.execute("DELETE FROM registroventa WHERE id_venta = %s AND sku_producto = %s LIMIT 1",
                               (id_venta, sku))
                print(f"Producto {sku} eliminado. Total actual: {total_venta}")
            else:
                print("Producto no encontrado en esta venta.")

        elif opcion == "3":
            # Actualizar el total en la tabla venta
            cursor.execute("UPDATE venta SET total = %s WHERE id_venta = %s", (total_venta, id_venta))
            conn.commit()
            print(f"Venta finalizada. Total: {total_venta}")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

    cursor.close()


def menu_vendedor(id_empleado):
    conexion = conectar_db()
    if conexion is None:
        return

    while True:
        print("\n--- MENÚ VENDEDOR ---")
        print("1. Registrar venta")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta(conexion, id_empleado)
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

    conexion.close()


def menu_principal():
    while True:
        print("\n=== Sistema de Gestión ===")
        print("1. Ingresar como Administrador")
        print("2. Ingresar como Encargado de Inventario")
        print("3. Ingresar como Soporte al Cliente")
        print("4. Ingresar como Especialista en Marketing")
        print("5. Ingresar como Vendedor")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            id_empleado = validar_usuario("administradorgeneral", usuario, contrasena)
            if id_empleado:
                menu_administrador()
            else:
                print("Usuario o contraseña incorrectos para Administrador.")

        elif opcion == "2":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            id_empleado = validar_usuario("encargadoinventario", usuario, contrasena)
            if id_empleado:
                menu_encargado_inventario(id_empleado)
            else:
                print("Usuario o contraseña incorrectos para Encargado de Inventario.")

        elif opcion == "3":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            id_empleado = validar_usuario("soportecliente", usuario, contrasena)
            if id_empleado:
                menu_soporte_cliente(id_empleado)
            else:
                print("Usuario o contraseña incorrectos para Soporte al Cliente.")

        elif opcion == "4":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            id_empleado = validar_usuario("especialistamarketing", usuario, contrasena)
            if id_empleado:
                menu_especialista_marketing(id_empleado)
            else:
                print("Usuario o contraseña incorrectos para Especialista en Marketing.")
        elif opcion == "5":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            id_empleado = validar_usuario("vendedor", usuario, contrasena)
            if id_empleado:
                menu_vendedor(id_empleado)
            else:
                print("Usuario o contraseña incorrectos para Vendedor.")

        elif opcion == "6":
            print("Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
