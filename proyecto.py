-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS SistemaEmpleados;
USE SistemaEmpleados;

-- Tabla Empleado
CREATE TABLE Empleado (
    ID_Empleado INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Usuario VARCHAR(50) NOT NULL UNIQUE,
    Contraseña VARCHAR(255) NOT NULL,
    Horario VARCHAR(50) NOT NULL
);

-- Tabla Administrador General (hereda de Empleado)
CREATE TABLE AdministradorGeneral (
    ID_Empleado INT PRIMARY KEY,
    FOREIGN KEY (ID_Empleado) REFERENCES Empleado(ID_Empleado)
);

-- Tabla Encargado de Inventario (hereda de Empleado)
CREATE TABLE EncargadoInventario (
    ID_Empleado INT PRIMARY KEY,
    FOREIGN KEY (ID_Empleado) REFERENCES Empleado(ID_Empleado)
);

-- Tabla Especialista en Marketing (hereda de Empleado)
CREATE TABLE EspecialistaMarketing (
    ID_Empleado INT PRIMARY KEY,
    FOREIGN KEY (ID_Empleado) REFERENCES Empleado(ID_Empleado)
);

-- Tabla Vendedor (hereda de Empleado)
CREATE TABLE Vendedor (
    ID_Empleado INT PRIMARY KEY,
    FOREIGN KEY (ID_Empleado) REFERENCES Empleado(ID_Empleado)
);

-- Tabla Soporte al Cliente (hereda de Empleado)
CREATE TABLE SoporteCliente (
    ID_Empleado INT PRIMARY KEY,
    FOREIGN KEY (ID_Empleado) REFERENCES Empleado(ID_Empleado)
);

-- Tabla Producto
CREATE TABLE Producto (
    ID_Producto INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    SKU VARCHAR(20) NOT NULL UNIQUE
);

-- Tabla Inventario
CREATE TABLE Inventario (
    ID_Inventario INT AUTO_INCREMENT PRIMARY KEY,
    ID_Producto INT NOT NULL,
    Cantidad_Stock INT NOT NULL,
    Fecha_Reposicion DATE,
    FOREIGN KEY (ID_Producto) REFERENCES Producto(ID_Producto)
);

-- Tabla Proveedor
CREATE TABLE Proveedor (
    ID_Proveedor INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Metodo_Contacto VARCHAR(50) NOT NULL
);

-- Tabla Cliente
CREATE TABLE Cliente (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Direccion VARCHAR(255),
    Telefono VARCHAR(15),
    Correo VARCHAR(100)
);

-- Tabla Venta
CREATE TABLE Venta (
    ID_Venta INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cliente INT NOT NULL,
    Total DECIMAL(10, 2) NOT NULL,
    Fecha DATE NOT NULL,
    Estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);

-- Tabla Factura
CREATE TABLE Factura (
    ID_Factura INT AUTO_INCREMENT PRIMARY KEY,
    ID_Venta INT NOT NULL,
    Fecha_Emision DATE NOT NULL,
    Numero_Factura VARCHAR(50) NOT NULL UNIQUE,
    Correo VARCHAR(100),
    Direccion VARCHAR(255),
    Telefono VARCHAR(15),
    FOREIGN KEY (ID_Venta) REFERENCES Venta(ID_Venta)
);

-- Tabla Oferta
CREATE TABLE Oferta (
    ID_Oferta INT AUTO_INCREMENT PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL,
    Fecha_Inicio DATE NOT NULL,
    Fecha_Fin DATE NOT NULL
);

-- Tabla Red Social
CREATE TABLE RedSocial (
    ID_RedSocial INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    URL VARCHAR(255) NOT NULL UNIQUE
);

-- Inserción de datos iniciales (ejemplo con 10 registros por tabla)
INSERT INTO Empleado (Nombre, Usuario, Contraseña, Horario) VALUES
('Juan Pérez', 'jperez', 'password1', '08:00-17:00'),
('María Gómez', 'mgomez', 'password2', '09:00-18:00'),
('Luis Martínez', 'lmartinez', 'password3', '07:00-16:00'),
('Ana López', 'alopez', 'password4', '10:00-19:00'),
('Carlos Ruiz', 'cruiz', 'password5', '08:30-17:30'),
('Elena Torres', 'etorres', 'password6', '09:00-18:00'),
('Roberto Díaz', 'rdiaz', 'password7', '07:30-16:30'),
('Laura Sánchez', 'lsanchez', 'password8', '10:30-19:30'),
('Fernando García', 'fgarcia', 'password9', '08:00-17:00'),
('Gabriela Vargas', 'gvargas', 'password10', '09:30-18:30');

INSERT INTO Producto (Nombre, Categoria, Precio, SKU) VALUES
('Producto A', 'Categoría 1', 10.50, 'SKU001'),
('Producto B', 'Categoría 1', 20.00, 'SKU002'),
('Producto C', 'Categoría 2', 15.75, 'SKU003'),
('Producto D', 'Categoría 2', 18.00, 'SKU004'),
('Producto E', 'Categoría 3', 12.50, 'SKU005'),
('Producto F', 'Categoría 3', 30.00, 'SKU006'),
('Producto G', 'Categoría 1', 25.00, 'SKU007'),
('Producto H', 'Categoría 2', 17.00, 'SKU008'),
('Producto I', 'Categoría 3', 22.50, 'SKU009'),
('Producto J', 'Categoría 1', 19.75, 'SKU010');

INSERT INTO Inventario (ID_Producto, Cantidad_Stock, Fecha_Reposicion) VALUES
(1, 100, '2024-12-01'),
(2, 200, '2024-12-02'),
(3, 150, '2024-12-03'),
(4, 80, '2024-12-04'),
(5, 120, '2024-12-05'),
(6, 50, '2024-12-06'),
(7, 300, '2024-12-07'),
(8, 90, '2024-12-08'),
(9, 70, '2024-12-09'),
(10, 110, '2024-12-10');

INSERT INTO Proveedor (Nombre, Direccion, Metodo_Contacto) VALUES
('Proveedor A', 'Dirección 1', 'Teléfono'),
('Proveedor B', 'Dirección 2', 'Email'),
('Proveedor C', 'Dirección 3', 'Teléfono'),
('Proveedor D', 'Dirección 4', 'Email'),
('Proveedor E', 'Dirección 5', 'Teléfono'),
('Proveedor F', 'Dirección 6', 'Email'),
('Proveedor G', 'Dirección 7', 'Teléfono'),
('Proveedor H', 'Dirección 8', 'Email'),
('Proveedor I', 'Dirección 9', 'Teléfono'),
('Proveedor J', 'Dirección 10', 'Email');

INSERT INTO Cliente (Nombre, Direccion, Telefono, Correo) VALUES
('Cliente A', 'Dirección 1', '123456789', 'clienteA@example.com'),
('Cliente B', 'Dirección 2', '987654321', 'clienteB@example.com'),
('Cliente C', 'Dirección 3', '123123123', 'clienteC@example.com'),
('Cliente D', 'Dirección 4', '456456456', 'clienteD@example.com'),
('Cliente E', 'Dirección 5', '789789789', 'clienteE@example.com'),
('Cliente F', 'Dirección 6', '321321321', 'clienteF@example.com'),
('Cliente G', 'Dirección 7', '654654654', 'clienteG@example.com'),
('Cliente H', 'Dirección 8', '987987987', 'clienteH@example.com'),
('Cliente I', 'Dirección 9', '112233445', 'clienteI@example.com'),
('Cliente J', 'Dirección 10', '998877665', 'clienteJ@example.com');

INSERT INTO Venta (ID_Cliente, Total, Fecha, Estado) VALUES
(1, 100.50, '2024-12-01', 'Pagada'),
(2, 200.00, '2024-12-02', 'Pendiente'),
(3, 150.75, '2024-12-03', 'Pagada'),
(4, 80.00, '2024-12-04', 'Cancelada'),
(5, 120.50, '2024-12-05', 'Pendiente'),
(6, 50.00, '2024-12-06', 'Pagada'),
(7, 300.25, '2024-12-07', 'Pendiente'),
(8, 90.75, '2024-12-08', 'Pagada'),
(9, 70.50, '2024-12-09', 'Cancelada'),
(10, 110.25, '2024-12-10', 'Pagada');

INSERT INTO Factura (ID_Venta, Fecha_Emision, Numero_Factura, Correo, Direccion, Telefono) VALUES
(1, '2024-12-01', 'F001', 'clienteA@example.com', 'Dirección 1', '123456789'),
(2, '2024-12-02', 'F002', 'clienteB@example.com', 'Dirección 2', '987654321'),
(3, '2024-12-03', 'F003', 'clienteC@example.com', 'Dirección 3', '123123123'),
(4, '2024-12-04', 'F004', 'clienteD@example.com', 'Dirección 4', '456456456'),
(5, '2024-12-05', 'F005', 'clienteE@example.com', 'Dirección 5', '789789789'),
(6, '2024-12-06', 'F006', 'clienteF@example.com', 'Dirección 6', '321321321'),
(7, '2024-12-07', 'F007', 'clienteG@example.com', 'Dirección 7', '654654654'),
(8, '2024-12-08', 'F008', 'clienteH@example.com', 'Dirección 8', '987987987'),
(9, '2024-12-09', 'F009', 'clienteI@example.com', 'Dirección 9', '112233445'),
(10, '2024-12-10', 'F010', 'clienteJ@example.com', 'Dirección 10', '998877665');

INSERT INTO Oferta (Descripcion, Fecha_Inicio, Fecha_Fin) VALUES
('Oferta 1', '2024-12-01', '2024-12-10'),
('Oferta 2', '2024-12-11', '2024-12-20'),
('Oferta 3', '2024-12-21', '2024-12-30'),
('Oferta 4', '2025-01-01', '2025-01-10'),
('Oferta 5', '2025-01-11', '2025-01-20'),
('Oferta 6', '2025-01-21', '2025-01-30'),
('Oferta 7', '2025-02-01', '2025-02-10'),
('Oferta 8', '2025-02-11', '2025-02-20'),
('Oferta 9', '2025-02-21', '2025-02-28'),
('Oferta 10', '2025-03-01', '2025-03-10');

INSERT INTO RedSocial (Nombre, URL) VALUES
('Facebook', 'https://www.facebook.com'),
('Twitter', 'https://www.twitter.com'),
('Instagram', 'https://www.instagram.com'),
('LinkedIn', 'https://www.linkedin.com'),
('Pinterest', 'https://www.pinterest.com'),
('Snapchat', 'https://www.snapchat.com'),
('TikTok', 'https://www.tiktok.com'),
('YouTube', 'https://www.youtube.com'),
('Reddit', 'https://www.reddit.com'),
('WhatsApp', 'https://www.whatsapp.com');
