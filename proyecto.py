import mysql.connector

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

# Menú de la aplicación
def menu():
    while True:
        print("\n=== Gestión de Empleados ===")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Eliminar empleado")
        print("4. Salir")

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
            print("Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()