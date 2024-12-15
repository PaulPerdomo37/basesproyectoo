import mysql.connector
from mysql.connector.dbapi import DATETIME

def conectar_db():
    """Conecta a la base de datos MySQL usando XAMPP."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Usuario por defecto en XAMPP
            password="",  # Sin contraseña por defecto en XAMPP
            database="SistemaEmpleados"  # Nombre correcto de la base de datos
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def agregar_empleado(nombre, usuario, contrasena, horario):
    """Agrega un empleado a la base de datos."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = (
                "INSERT INTO Empleado (Nombre, Usuario, Contraseña, Horario) "
                "VALUES (%s, %s, %s, %s)"
            )
            valores = (nombre, usuario, contrasena, horario)
            cursor.execute(query, valores)
            conexion.commit()
            print("Empleado agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar empleado: {err}")
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

def eliminar_empleado(id_empleado):
    """Elimina un empleado por ID."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM Empleado WHERE ID_Empleado = %s"
            cursor.execute(query, (id_empleado,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Empleado eliminado exitosamente.")
            else:
                print("No se encontró un empleado con ese ID.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar empleado: {err}")
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

def menu_administrador():
    """Muestra el menú de administrador."""
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Eliminar empleado")
        print("4. Agendar empleado en tipo de usuario")
        print("5. Eliminar empleado de tipo de usuario")
        print("6. Volver al menú principal")

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
            id_empleado = int(input("ID del empleado a agendar: "))
            tipo_usuario = input("Tipo de usuario (administrador, soporte, vendedor, marketing, inventario): ")
            agendar_usuario(id_empleado, tipo_usuario)
        elif opcion == "5":
            id_empleado = int(input("ID del empleado a eliminar: "))
            tipo_usuario = input("Tipo de usuario (administrador, soporte, vendedor, marketing, inventario): ")
            eliminar_usuario_tipo(id_empleado, tipo_usuario)
        elif opcion == "6":
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
    """Actualiza un campo específico de un producto en la base de datos."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = f"UPDATE producto SET {campo} = %s WHERE sku = %s"
            cursor.execute(query, (nuevo_valor, id_producto))
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
            fecha_actual = DATETIME.now().strftime('%Y-%m-%d %H:%M:%S')
            query = (
                "INSERT INTO gestion (id_encargadodeinventario, id_producto, descripcion, fecha) "
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

def menu_encargado_inventario():
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



def menu_soporte_cliente():
    """Muestra el menú de soporte al cliente."""
    print("\n=== Menú Soporte al Cliente ===")
    print("Acceso a funciones relacionadas con soporte al cliente aún no implementadas.")

def menu_especialista_marketing():
    """Muestra el menú del especialista en marketing."""
    print("\n=== Menú Especialista en Marketing ===")
    print("Acceso a funciones relacionadas con marketing aún no implementadas.")

def menu_principal():
    while True:
        print("\n=== Sistema de Gestión ===")
        print("1. Ingresar como Administrador")
        print("2. Ingresar como Encargado de Inventario")
        print("3. Ingresar como Soporte al Cliente")
        print("4. Ingresar como Especialista en Marketing")
        print("5. Salir")

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
                menu_soporte_cliente()
            else:
                print("Usuario o contraseña incorrectos para Soporte al Cliente.")

        elif opcion == "4":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            id_empleado = validar_usuario("especialistamarketing", usuario, contrasena)
            if id_empleado:
                menu_especialista_marketing()
            else:
                print("Usuario o contraseña incorrectos para Especialista en Marketing.")

        elif opcion == "5":
            print("Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
