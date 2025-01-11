-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-01-2025 a las 01:53:15
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
  `ID_Empleado` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Horario` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `administradorgeneral`
--

INSERT INTO `administradorgeneral` (`ID_Empleado`, `Nombre`, `Usuario`, `Contraseña`, `Horario`) VALUES
(1, 'Juan Pérez', 'jperez', 'password1', '08:00-17:00'),
(2, 'María Gómez', 'mgomez', 'password2', '09:00-18:00'),
(3, 'Luis Martínez', 'lmartinez', 'password3', '07:00-16:00'),
(4, 'Ana López', 'alopez', 'password4', '10:00-19:00'),
(5, 'Carlos Ruiz', 'cruiz', 'password5', '08:30-17:30'),
(6, 'Elena Torres', 'etorres', 'password6', '09:00-18:00'),
(7, 'Roberto Díaz', 'rdiaz', 'password7', '07:30-16:30'),
(8, 'Laura Sánchez', 'lsanchez', 'password8', '10:30-19:30'),
(9, 'Fernando García', 'fgarcia', 'password9', '08:00-17:00'),
(10, 'Gabriela Vargas', 'gvargas', 'password10', '09:30-18:30'),
(12, 'Claudia Romero', 'cromero', 'password11', '08:00-17:00'),
(13, 'Mario Hernández', 'mhernandez', 'password12', '09:00-18:00');

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
(10, 'Gabriela Vargas', 'gvargas', 'password10', '09:30-18:30'),
(12, 'Claudia Romero', 'cromero', 'password11', '08:00-17:00'),
(13, 'Mario Hernández', 'mhernandez', 'password12', '09:00-18:00'),
(14, 'Sofía Jiménez', 'sjimenez', 'password13', '10:00-19:00'),
(15, 'Ricardo Peña', 'rpena', 'password14', '07:00-16:00'),
(16, 'Valeria Castro', 'vcastro', 'password15', '08:30-17:30'),
(17, 'Diego Méndez', 'dmendez', 'password16', '09:00-18:00'),
(18, 'Rosa Gutiérrez', 'rgutierrez', 'password17', '07:30-16:30'),
(19, 'Pablo Vargas', 'pvargas', 'password18', '10:30-19:30'),
(20, 'Andrea Flores', 'aflores', 'password19', '08:00-17:00'),
(21, 'Hugo Morales', 'hmorales', 'password20', '09:30-18:30'),
(22, 'Isabel Cruz', 'icruz', 'password21', '08:00-17:00'),
(23, 'Camila Reyes', 'creyes', 'password22', '09:00-18:00'),
(24, 'Juan Torres', 'jtorres', 'password23', '10:00-19:00'),
(25, 'Miguel Campos', 'mcampos', 'password24', '07:00-16:00'),
(26, 'Paula Ortiz', 'portiz', 'password25', '08:30-17:30'),
(27, 'Emilio Rojas', 'erojas', 'password26', '09:00-18:00'),
(29, 'Jorge López', 'jlopez', 'password28', '10:30-19:30'),
(30, 'Karina Díaz', 'kdiaz', 'password29', '08:00-17:00'),
(33, 'prueba', 'pr', 's', '08:00-12:00'),
(35, 'p', 'p', 'p', '9:00-10:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encargadoinventario`
--

CREATE TABLE `encargadoinventario` (
  `ID_Empleado` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Horario` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `encargadoinventario`
--

INSERT INTO `encargadoinventario` (`ID_Empleado`, `Nombre`, `Usuario`, `Contraseña`, `Horario`) VALUES
(18, 'Rosa Gutiérrez', 'rgutierrez', 'password17', '07:30-16:30'),
(19, 'Pablo Vargas', 'pvargas', 'password18', '10:30-19:30'),
(20, 'Andrea Flores', 'aflores', 'password19', '08:00-17:00'),
(21, 'Hugo Morales', 'hmorales', 'password20', '09:30-18:30'),
(22, 'Isabel Cruz', 'icruz', 'password21', '08:00-17:00'),
(23, 'Camila Reyes', 'creyes', 'password22', '09:00-18:00'),
(24, 'Juan Torres', 'jtorres', 'password23', '10:00-19:00'),
(25, 'Miguel Campos', 'mcampos', 'password24', '07:00-16:00'),
(26, 'Paula Ortiz', 'portiz', 'password25', '08:30-17:30'),
(33, 'prueba', 'pr', 's', '08:00-12:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialistamarketing`
--

CREATE TABLE `especialistamarketing` (
  `ID_Empleado` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Horario` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `especialistamarketing`
--

INSERT INTO `especialistamarketing` (`ID_Empleado`, `Nombre`, `Usuario`, `Contraseña`, `Horario`) VALUES
(7, 'Roberto Díaz', 'rdiaz', 'password7', '07:30-16:30'),
(8, 'Laura Sánchez', 'lsanchez', 'password8', '10:30-19:30'),
(9, 'Fernando García', 'fgarcia', 'password9', '08:00-17:00'),
(10, 'Gabriela Vargas', 'gvargas', 'password10', '09:30-18:30'),
(12, 'Claudia Romero', 'cromero', 'password11', '08:00-17:00'),
(13, 'Mario Hernández', 'mhernandez', 'password12', '09:00-18:00'),
(14, 'Sofía Jiménez', 'sjimenez', 'password13', '10:00-19:00'),
(15, 'Ricardo Peña', 'rpena', 'password14', '07:00-16:00'),
(16, 'Valeria Castro', 'vcastro', 'password15', '08:30-17:30'),
(17, 'Diego Méndez', 'dmendez', 'password16', '09:00-18:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestion`
--

CREATE TABLE `gestion` (
  `id_gestion` int(11) NOT NULL,
  `id_empleado` int(11) DEFAULT NULL,
  `sku` varchar(50) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `gestion`
--

INSERT INTO `gestion` (`id_gestion`, `id_empleado`, `sku`, `descripcion`, `fecha`) VALUES
(1, 22, 'SKU5', 'Stock actualizado', '2024-12-15'),
(2, 20, 'SKU1', 'Stock actualizado y categoria tambien', '2024-12-16'),
(3, 19, 'SKU1', 'Stock actualizado, Nombre actualizado', '2024-12-16');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestionoferta`
--

CREATE TABLE `gestionoferta` (
  `ID_Empleado` int(11) NOT NULL,
  `id_oferta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `oferta`
--

CREATE TABLE `oferta` (
  `id_oferta` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_final` date NOT NULL,
  `sku` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `porcentaje_descuento` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `oferta`
--

INSERT INTO `oferta` (`id_oferta`, `fecha_inicio`, `fecha_final`, `sku`, `descripcion`, `porcentaje_descuento`) VALUES
(1, '2024-01-01', '2024-01-31', 'SKU1', 'Oferta A', 5),
(2, '2024-02-01', '2024-02-28', 'SKU2', 'Oferta B', 10),
(3, '2024-03-01', '2024-03-31', 'SKU3', 'Oferta C', 15),
(4, '2024-04-01', '2024-04-30', 'SKU4', 'Oferta D', 20),
(5, '2024-05-01', '2024-05-31', 'SKU5', 'Oferta E', 25),
(6, '2024-06-01', '2024-06-30', 'SKU6', 'Oferta F', 30),
(7, '2024-07-01', '2024-07-31', 'SKU7', 'Oferta G', 35),
(8, '2024-08-01', '2024-08-31', 'SKU8', 'Oferta H', 40),
(9, '2024-09-01', '2024-09-30', 'SKU9', 'Oferta I', 45),
(10, '2024-10-01', '2024-10-31', 'SKU10', 'Oferta J', 50),
(11, '2023-12-10', '2023-12-11', 'SKU1', 's', 0.1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `sku` varchar(50) NOT NULL,
  `categoria` varchar(100) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `id_proveedor` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`sku`, `categoria`, `nombre`, `precio`, `id_proveedor`, `stock`) VALUES
('SKU1', 'Anime', 'Mansion', '20.00', 1, 47),
('SKU10', 'Categoria J', 'Producto J', '100.00', 10, 1000),
('SKU2', 'Categoria B', 'Producto B', '20.00', 2, 2),
('SKU3', 'Categoria A', 'Producto C', '30.00', 3, 300),
('SKU4', 'Categoria D', 'Producto D', '40.00', 4, 400),
('SKU5', 'Categoria E', 'Producto E', '50.00', 5, 10),
('SKU6', 'Categoria F', 'Producto F', '60.00', 6, 600),
('SKU7', 'Categoria G', 'Producto G', '70.00', 7, 700),
('SKU8', 'Categoria H', 'Producto H', '80.00', 8, 800),
('SKU9', 'Categoria I', 'Producto I', '90.00', 9, 900);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `promociona`
--

CREATE TABLE `promociona` (
  `id_oferta` int(11) NOT NULL,
  `ID_RedSocial` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `promociona`
--

INSERT INTO `promociona` (`id_oferta`, `ID_RedSocial`, `fecha_inicio`) VALUES
(1, 1, '2024-01-05'),
(2, 2, '2024-02-05'),
(3, 3, '2024-03-05'),
(4, 4, '2024-04-05'),
(5, 5, '2024-05-05'),
(6, 6, '2024-06-05'),
(7, 7, '2024-07-05'),
(8, 8, '2024-08-05'),
(9, 9, '2024-02-01');

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
-- Estructura de tabla para la tabla `registroventa`
--

CREATE TABLE `registroventa` (
  `id_venta` int(11) NOT NULL,
  `sku_producto` varchar(50) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registroventa`
--

INSERT INTO `registroventa` (`id_venta`, `sku_producto`, `fecha`) VALUES
(1, 'SKU4', '2024-12-16'),
(2, 'SKU1', '2024-12-16'),
(2, 'SKU10', '2024-12-16');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `soportecliente`
--

CREATE TABLE `soportecliente` (
  `ID_Empleado` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Horario` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `soportecliente`
--

INSERT INTO `soportecliente` (`ID_Empleado`, `Nombre`, `Usuario`, `Contraseña`, `Horario`) VALUES
(14, 'Sofía Jiménez', 'sjimenez', 'password13', '10:00-19:00'),
(15, 'Ricardo Peña', 'rpena', 'password14', '07:00-16:00'),
(16, 'Valeria Castro', 'vcastro', 'password15', '08:30-17:30'),
(17, 'Diego Méndez', 'dmendez', 'password16', '09:00-18:00'),
(18, 'Rosa Gutiérrez', 'rgutierrez', 'password17', '07:30-16:30'),
(19, 'Pablo Vargas', 'pvargas', 'password18', '10:30-19:30'),
(20, 'Andrea Flores', 'aflores', 'password19', '08:00-17:00'),
(21, 'Hugo Morales', 'hmorales', 'password20', '09:30-18:30'),
(22, 'Isabel Cruz', 'icruz', 'password21', '08:00-17:00'),
(23, 'Camila Reyes', 'creyes', 'password22', '09:00-18:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

CREATE TABLE `vendedor` (
  `ID_Empleado` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Horario` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `vendedor`
--

INSERT INTO `vendedor` (`ID_Empleado`, `Nombre`, `Usuario`, `Contraseña`, `Horario`) VALUES
(1, 'Juan Pérez', 'jperez', 'password1', '08:00-17:00'),
(2, 'María Gómez', 'mgomez', 'password2', '09:00-18:00'),
(3, 'Luis Martínez', 'lmartinez', 'password3', '07:00-16:00'),
(4, 'Ana López', 'alopez', 'password4', '10:00-19:00'),
(5, 'Carlos Ruiz', 'cruiz', 'password5', '08:30-17:30'),
(6, 'Elena Torres', 'etorres', 'password6', '09:00-18:00'),
(24, 'Juan Torres', 'jtorres', 'password23', '10:00-19:00'),
(25, 'Miguel Campos', 'mcampos', 'password24', '07:00-16:00'),
(26, 'Paula Ortiz', 'portiz', 'password25', '08:30-17:30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id_venta` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`id_venta`, `id_cliente`, `id_empleado`, `fecha`, `total`) VALUES
(1, 1, 1, '2024-12-16', '20.00'),
(2, 1, 1, '2024-12-16', '120.00');

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
-- Indices de la tabla `gestion`
--
ALTER TABLE `gestion`
  ADD PRIMARY KEY (`id_gestion`),
  ADD KEY `id_empleado` (`id_empleado`),
  ADD KEY `sku` (`sku`);

--
-- Indices de la tabla `gestionoferta`
--
ALTER TABLE `gestionoferta`
  ADD PRIMARY KEY (`ID_Empleado`,`id_oferta`),
  ADD KEY `id_oferta` (`id_oferta`);

--
-- Indices de la tabla `oferta`
--
ALTER TABLE `oferta`
  ADD PRIMARY KEY (`id_oferta`),
  ADD KEY `sku` (`sku`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`sku`),
  ADD KEY `id_proveedor` (`id_proveedor`);

--
-- Indices de la tabla `promociona`
--
ALTER TABLE `promociona`
  ADD PRIMARY KEY (`id_oferta`,`ID_RedSocial`),
  ADD KEY `ID_RedSocial` (`ID_RedSocial`);

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
-- Indices de la tabla `registroventa`
--
ALTER TABLE `registroventa`
  ADD KEY `id_venta` (`id_venta`),
  ADD KEY `sku_producto` (`sku_producto`);

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
  ADD PRIMARY KEY (`id_venta`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_empleado` (`id_empleado`);

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
  MODIFY `ID_Empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `gestion`
--
ALTER TABLE `gestion`
  MODIFY `id_gestion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `oferta`
--
ALTER TABLE `oferta`
  MODIFY `id_oferta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

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
  MODIFY `id_venta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
-- Filtros para la tabla `gestion`
--
ALTER TABLE `gestion`
  ADD CONSTRAINT `gestion_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `encargadoinventario` (`ID_Empleado`),
  ADD CONSTRAINT `gestion_ibfk_2` FOREIGN KEY (`sku`) REFERENCES `producto` (`sku`);

--
-- Filtros para la tabla `gestionoferta`
--
ALTER TABLE `gestionoferta`
  ADD CONSTRAINT `gestionoferta_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `especialistamarketing` (`ID_Empleado`),
  ADD CONSTRAINT `gestionoferta_ibfk_2` FOREIGN KEY (`id_oferta`) REFERENCES `oferta` (`id_oferta`);

--
-- Filtros para la tabla `oferta`
--
ALTER TABLE `oferta`
  ADD CONSTRAINT `oferta_ibfk_1` FOREIGN KEY (`sku`) REFERENCES `producto` (`sku`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`ID_Proveedor`);

--
-- Filtros para la tabla `promociona`
--
ALTER TABLE `promociona`
  ADD CONSTRAINT `promociona_ibfk_1` FOREIGN KEY (`id_oferta`) REFERENCES `oferta` (`id_oferta`),
  ADD CONSTRAINT `promociona_ibfk_2` FOREIGN KEY (`ID_RedSocial`) REFERENCES `redsocial` (`ID_RedSocial`);

--
-- Filtros para la tabla `registroventa`
--
ALTER TABLE `registroventa`
  ADD CONSTRAINT `registroventa_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`);

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
  ADD CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`ID_Cliente`),
  ADD CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`id_empleado`) REFERENCES `vendedor` (`ID_Empleado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
