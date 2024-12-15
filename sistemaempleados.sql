-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-12-2024 a las 18:30:44
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistemaempleados`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradorgeneral`
--

CREATE TABLE `administradorgeneral` (
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `ID_Cliente` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Direccion` varchar(255) DEFAULT NULL,
  `Telefono` varchar(15) DEFAULT NULL,
  `Correo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`ID_Cliente`, `Nombre`, `Direccion`, `Telefono`, `Correo`) VALUES
(1, 'Cliente A', 'Dirección 1', '123456789', 'clienteA@example.com'),
(2, 'Cliente B', 'Dirección 2', '987654321', 'clienteB@example.com'),
(3, 'Cliente C', 'Dirección 3', '123123123', 'clienteC@example.com'),
(4, 'Cliente D', 'Dirección 4', '456456456', 'clienteD@example.com'),
(5, 'Cliente E', 'Dirección 5', '789789789', 'clienteE@example.com'),
(6, 'Cliente F', 'Dirección 6', '321321321', 'clienteF@example.com'),
(7, 'Cliente G', 'Dirección 7', '654654654', 'clienteG@example.com'),
(8, 'Cliente H', 'Dirección 8', '987987987', 'clienteH@example.com'),
(9, 'Cliente I', 'Dirección 9', '112233445', 'clienteI@example.com'),
(10, 'Cliente J', 'Dirección 10', '998877665', 'clienteJ@example.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `ID_Empleado` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Horario` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`ID_Empleado`, `Nombre`, `Usuario`, `Contraseña`, `Horario`) VALUES
(1, 'Juan Pérez', 'jperez', 'password1', '08:00-17:00'),
(2, 'María Gómez', 'mgomez', 'password2', '09:00-18:00'),
(3, 'Luis Martínez', 'lmartinez', 'password3', '07:00-16:00'),
(4, 'Ana López', 'alopez', 'password4', '10:00-19:00'),
(5, 'Carlos Ruiz', 'cruiz', 'password5', '08:30-17:30'),
(6, 'Elena Torres', 'etorres', 'password6', '09:00-18:00'),
(7, 'Roberto Díaz', 'rdiaz', 'password7', '07:30-16:30'),
(8, 'Laura Sánchez', 'lsanchez', 'password8', '10:30-19:30'),
(9, 'Fernando García', 'fgarcia', 'password9', '08:00-17:00'),
(10, 'Gabriela Vargas', 'gvargas', 'password10', '09:30-18:30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encargadoinventario`
--

CREATE TABLE `encargadoinventario` (
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialistamarketing`
--

CREATE TABLE `especialistamarketing` (
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `ID_Factura` int(11) NOT NULL,
  `ID_Venta` int(11) NOT NULL,
  `Fecha_Emision` date NOT NULL,
  `Numero_Factura` varchar(50) NOT NULL,
  `Correo` varchar(100) DEFAULT NULL,
  `Direccion` varchar(255) DEFAULT NULL,
  `Telefono` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `factura`
--

INSERT INTO `factura` (`ID_Factura`, `ID_Venta`, `Fecha_Emision`, `Numero_Factura`, `Correo`, `Direccion`, `Telefono`) VALUES
(1, 1, '2024-12-01', 'F001', 'clienteA@example.com', 'Dirección 1', '123456789'),
(2, 2, '2024-12-02', 'F002', 'clienteB@example.com', 'Dirección 2', '987654321'),
(3, 3, '2024-12-03', 'F003', 'clienteC@example.com', 'Dirección 3', '123123123'),
(4, 4, '2024-12-04', 'F004', 'clienteD@example.com', 'Dirección 4', '456456456'),
(5, 5, '2024-12-05', 'F005', 'clienteE@example.com', 'Dirección 5', '789789789'),
(6, 6, '2024-12-06', 'F006', 'clienteF@example.com', 'Dirección 6', '321321321'),
(7, 7, '2024-12-07', 'F007', 'clienteG@example.com', 'Dirección 7', '654654654'),
(8, 8, '2024-12-08', 'F008', 'clienteH@example.com', 'Dirección 8', '987987987'),
(9, 9, '2024-12-09', 'F009', 'clienteI@example.com', 'Dirección 9', '112233445'),
(10, 10, '2024-12-10', 'F010', 'clienteJ@example.com', 'Dirección 10', '998877665');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `ID_Inventario` int(11) NOT NULL,
  `ID_Producto` int(11) NOT NULL,
  `Cantidad_Stock` int(11) NOT NULL,
  `Fecha_Reposicion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`ID_Inventario`, `ID_Producto`, `Cantidad_Stock`, `Fecha_Reposicion`) VALUES
(1, 1, 100, '2024-12-01'),
(2, 2, 200, '2024-12-02'),
(3, 3, 150, '2024-12-03'),
(4, 4, 80, '2024-12-04'),
(5, 5, 120, '2024-12-05'),
(6, 6, 50, '2024-12-06'),
(7, 7, 300, '2024-12-07'),
(8, 8, 90, '2024-12-08'),
(9, 9, 70, '2024-12-09'),
(10, 10, 110, '2024-12-10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `oferta`
--

CREATE TABLE `oferta` (
  `ID_Oferta` int(11) NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `Fecha_Inicio` date NOT NULL,
  `Fecha_Fin` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `oferta`
--

INSERT INTO `oferta` (`ID_Oferta`, `Descripcion`, `Fecha_Inicio`, `Fecha_Fin`) VALUES
(1, 'Oferta 1', '2024-12-01', '2024-12-10'),
(2, 'Oferta 2', '2024-12-11', '2024-12-20'),
(3, 'Oferta 3', '2024-12-21', '2024-12-30'),
(4, 'Oferta 4', '2025-01-01', '2025-01-10'),
(5, 'Oferta 5', '2025-01-11', '2025-01-20'),
(6, 'Oferta 6', '2025-01-21', '2025-01-30'),
(7, 'Oferta 7', '2025-02-01', '2025-02-10'),
(8, 'Oferta 8', '2025-02-11', '2025-02-20'),
(9, 'Oferta 9', '2025-02-21', '2025-02-28'),
(10, 'Oferta 10', '2025-03-01', '2025-03-10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `ID_Producto` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Categoria` varchar(50) NOT NULL,
  `Precio` decimal(10,2) NOT NULL,
  `SKU` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`ID_Producto`, `Nombre`, `Categoria`, `Precio`, `SKU`) VALUES
(1, 'Producto A', 'Categoría 1', '10.50', 'SKU001'),
(2, 'Producto B', 'Categoría 1', '20.00', 'SKU002'),
(3, 'Producto C', 'Categoría 2', '15.75', 'SKU003'),
(4, 'Producto D', 'Categoría 2', '18.00', 'SKU004'),
(5, 'Producto E', 'Categoría 3', '12.50', 'SKU005'),
(6, 'Producto F', 'Categoría 3', '30.00', 'SKU006'),
(7, 'Producto G', 'Categoría 1', '25.00', 'SKU007'),
(8, 'Producto H', 'Categoría 2', '17.00', 'SKU008'),
(9, 'Producto I', 'Categoría 3', '22.50', 'SKU009'),
(10, 'Producto J', 'Categoría 1', '19.75', 'SKU010');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `ID_Proveedor` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Direccion` varchar(255) NOT NULL,
  `Metodo_Contacto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`ID_Proveedor`, `Nombre`, `Direccion`, `Metodo_Contacto`) VALUES
(1, 'Proveedor A', 'Dirección 1', 'Teléfono'),
(2, 'Proveedor B', 'Dirección 2', 'Email'),
(3, 'Proveedor C', 'Dirección 3', 'Teléfono'),
(4, 'Proveedor D', 'Dirección 4', 'Email'),
(5, 'Proveedor E', 'Dirección 5', 'Teléfono'),
(6, 'Proveedor F', 'Dirección 6', 'Email'),
(7, 'Proveedor G', 'Dirección 7', 'Teléfono'),
(8, 'Proveedor H', 'Dirección 8', 'Email'),
(9, 'Proveedor I', 'Dirección 9', 'Teléfono'),
(10, 'Proveedor J', 'Dirección 10', 'Email');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `redsocial`
--

CREATE TABLE `redsocial` (
  `ID_RedSocial` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `URL` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `redsocial`
--

INSERT INTO `redsocial` (`ID_RedSocial`, `Nombre`, `URL`) VALUES
(1, 'Facebook', 'https://www.facebook.com'),
(2, 'Twitter', 'https://www.twitter.com'),
(3, 'Instagram', 'https://www.instagram.com'),
(4, 'LinkedIn', 'https://www.linkedin.com'),
(5, 'Pinterest', 'https://www.pinterest.com'),
(6, 'Snapchat', 'https://www.snapchat.com'),
(7, 'TikTok', 'https://www.tiktok.com'),
(8, 'YouTube', 'https://www.youtube.com'),
(9, 'Reddit', 'https://www.reddit.com'),
(10, 'WhatsApp', 'https://www.whatsapp.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `soportecliente`
--

CREATE TABLE `soportecliente` (
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

CREATE TABLE `vendedor` (
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `ID_Venta` int(11) NOT NULL,
  `ID_Cliente` int(11) NOT NULL,
  `Total` decimal(10,2) NOT NULL,
  `Fecha` date NOT NULL,
  `Estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`ID_Venta`, `ID_Cliente`, `Total`, `Fecha`, `Estado`) VALUES
(1, 1, '100.50', '2024-12-01', 'Pagada'),
(2, 2, '200.00', '2024-12-02', 'Pendiente'),
(3, 3, '150.75', '2024-12-03', 'Pagada'),
(4, 4, '80.00', '2024-12-04', 'Cancelada'),
(5, 5, '120.50', '2024-12-05', 'Pendiente'),
(6, 6, '50.00', '2024-12-06', 'Pagada'),
(7, 7, '300.25', '2024-12-07', 'Pendiente'),
(8, 8, '90.75', '2024-12-08', 'Pagada'),
(9, 9, '70.50', '2024-12-09', 'Cancelada'),
(10, 10, '110.25', '2024-12-10', 'Pagada');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradorgeneral`
--
ALTER TABLE `administradorgeneral`
  ADD PRIMARY KEY (`ID_Empleado`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`ID_Cliente`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`ID_Empleado`),
  ADD UNIQUE KEY `Usuario` (`Usuario`);

--
-- Indices de la tabla `encargadoinventario`
--
ALTER TABLE `encargadoinventario`
  ADD PRIMARY KEY (`ID_Empleado`);

--
-- Indices de la tabla `especialistamarketing`
--
ALTER TABLE `especialistamarketing`
  ADD PRIMARY KEY (`ID_Empleado`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`ID_Factura`),
  ADD UNIQUE KEY `Numero_Factura` (`Numero_Factura`),
  ADD KEY `ID_Venta` (`ID_Venta`);

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`ID_Inventario`),
  ADD KEY `ID_Producto` (`ID_Producto`);

--
-- Indices de la tabla `oferta`
--
ALTER TABLE `oferta`
  ADD PRIMARY KEY (`ID_Oferta`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`ID_Producto`),
  ADD UNIQUE KEY `SKU` (`SKU`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`ID_Proveedor`);

--
-- Indices de la tabla `redsocial`
--
ALTER TABLE `redsocial`
  ADD PRIMARY KEY (`ID_RedSocial`),
  ADD UNIQUE KEY `URL` (`URL`);

--
-- Indices de la tabla `soportecliente`
--
ALTER TABLE `soportecliente`
  ADD PRIMARY KEY (`ID_Empleado`);

--
-- Indices de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`ID_Empleado`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`ID_Venta`),
  ADD KEY `ID_Cliente` (`ID_Cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `ID_Cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `ID_Empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `ID_Factura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `ID_Inventario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `oferta`
--
ALTER TABLE `oferta`
  MODIFY `ID_Oferta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `ID_Producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `ID_Proveedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `redsocial`
--
ALTER TABLE `redsocial`
  MODIFY `ID_RedSocial` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `ID_Venta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administradorgeneral`
--
ALTER TABLE `administradorgeneral`
  ADD CONSTRAINT `administradorgeneral_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID_Empleado`);

--
-- Filtros para la tabla `encargadoinventario`
--
ALTER TABLE `encargadoinventario`
  ADD CONSTRAINT `encargadoinventario_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID_Empleado`);

--
-- Filtros para la tabla `especialistamarketing`
--
ALTER TABLE `especialistamarketing`
  ADD CONSTRAINT `especialistamarketing_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID_Empleado`);

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`ID_Venta`) REFERENCES `venta` (`ID_Venta`);

--
-- Filtros para la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD CONSTRAINT `inventario_ibfk_1` FOREIGN KEY (`ID_Producto`) REFERENCES `producto` (`ID_Producto`);

--
-- Filtros para la tabla `soportecliente`
--
ALTER TABLE `soportecliente`
  ADD CONSTRAINT `soportecliente_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID_Empleado`);

--
-- Filtros para la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD CONSTRAINT `vendedor_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID_Empleado`);

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`ID_Cliente`) REFERENCES `cliente` (`ID_Cliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
