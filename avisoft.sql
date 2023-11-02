-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-11-2023 a las 03:45:57
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `avisoft`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alimentacion`
--

CREATE TABLE IF NOT EXISTS `alimentacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `id_galpon` int(11) NOT NULL,
  `Gr/Gallina/Dia` int(11) NOT NULL,
  `kg_total` int(11) NOT NULL,
  `bultos_total` int(11) NOT NULL,
  `c_a` int(11) NOT NULL,
  `id_tipo_alimento` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_galpon` (`id_galpon`),
  KEY `id_tipo_alimento` (`id_tipo_alimento`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alimentacion`
--

INSERT INTO `alimentacion` (`id`, `fecha`, `id_galpon`, `Gr/Gallina/Dia`, `kg_total`, `bultos_total`, `c_a`, `id_tipo_alimento`) VALUES
(1, '2023-04-29', 4, 45, 23, 12, 23, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add alimentacion', 7, 'add_alimentacion'),
(26, 'Can change alimentacion', 7, 'change_alimentacion'),
(27, 'Can delete alimentacion', 7, 'delete_alimentacion'),
(28, 'Can view alimentacion', 7, 'view_alimentacion'),
(29, 'Can add detalle jornada', 8, 'add_detallejornada'),
(30, 'Can change detalle jornada', 8, 'change_detallejornada'),
(31, 'Can delete detalle jornada', 8, 'delete_detallejornada'),
(32, 'Can view detalle jornada', 8, 'view_detallejornada'),
(33, 'Can add estados', 9, 'add_estados'),
(34, 'Can change estados', 9, 'change_estados'),
(35, 'Can delete estados', 9, 'delete_estados'),
(36, 'Can view estados', 9, 'view_estados'),
(37, 'Can add ficha', 10, 'add_ficha'),
(38, 'Can change ficha', 10, 'change_ficha'),
(39, 'Can delete ficha', 10, 'delete_ficha'),
(40, 'Can view ficha', 10, 'view_ficha'),
(41, 'Can add gallinas', 11, 'add_gallinas'),
(42, 'Can change gallinas', 11, 'change_gallinas'),
(43, 'Can delete gallinas', 11, 'delete_gallinas'),
(44, 'Can view gallinas', 11, 'view_gallinas'),
(45, 'Can add galpones', 12, 'add_galpones'),
(46, 'Can change galpones', 12, 'change_galpones'),
(47, 'Can delete galpones', 12, 'delete_galpones'),
(48, 'Can view galpones', 12, 'view_galpones'),
(49, 'Can add jornada', 13, 'add_jornada'),
(50, 'Can change jornada', 13, 'change_jornada'),
(51, 'Can delete jornada', 13, 'delete_jornada'),
(52, 'Can view jornada', 13, 'view_jornada'),
(53, 'Can add linea', 14, 'add_linea'),
(54, 'Can change linea', 14, 'change_linea'),
(55, 'Can delete linea', 14, 'delete_linea'),
(56, 'Can view linea', 14, 'view_linea'),
(57, 'Can add mortalidad descarte', 15, 'add_mortalidaddescarte'),
(58, 'Can change mortalidad descarte', 15, 'change_mortalidaddescarte'),
(59, 'Can delete mortalidad descarte', 15, 'delete_mortalidaddescarte'),
(60, 'Can view mortalidad descarte', 15, 'view_mortalidaddescarte'),
(61, 'Can add produccion diaria', 16, 'add_producciondiaria'),
(62, 'Can change produccion diaria', 16, 'change_producciondiaria'),
(63, 'Can delete produccion diaria', 16, 'delete_producciondiaria'),
(64, 'Can view produccion diaria', 16, 'view_producciondiaria'),
(65, 'Can add rol', 17, 'add_rol'),
(66, 'Can change rol', 17, 'change_rol'),
(67, 'Can delete rol', 17, 'delete_rol'),
(68, 'Can view rol', 17, 'view_rol'),
(69, 'Can add tipo doc', 18, 'add_tipodoc'),
(70, 'Can change tipo doc', 18, 'change_tipodoc'),
(71, 'Can delete tipo doc', 18, 'delete_tipodoc'),
(72, 'Can view tipo doc', 18, 'view_tipodoc'),
(73, 'Can add tipos huevos', 19, 'add_tiposhuevos'),
(74, 'Can change tipos huevos', 19, 'change_tiposhuevos'),
(75, 'Can delete tipos huevos', 19, 'delete_tiposhuevos'),
(76, 'Can view tipos huevos', 19, 'view_tiposhuevos'),
(77, 'Can add usuario', 20, 'add_usuario'),
(78, 'Can change usuario', 20, 'change_usuario'),
(79, 'Can delete usuario', 20, 'delete_usuario'),
(80, 'Can view usuario', 20, 'view_usuario'),
(81, 'Can add auth group', 21, 'add_authgroup'),
(82, 'Can change auth group', 21, 'change_authgroup'),
(83, 'Can delete auth group', 21, 'delete_authgroup'),
(84, 'Can view auth group', 21, 'view_authgroup'),
(85, 'Can add auth group permissions', 22, 'add_authgrouppermissions'),
(86, 'Can change auth group permissions', 22, 'change_authgrouppermissions'),
(87, 'Can delete auth group permissions', 22, 'delete_authgrouppermissions'),
(88, 'Can view auth group permissions', 22, 'view_authgrouppermissions'),
(89, 'Can add auth permission', 23, 'add_authpermission'),
(90, 'Can change auth permission', 23, 'change_authpermission'),
(91, 'Can delete auth permission', 23, 'delete_authpermission'),
(92, 'Can view auth permission', 23, 'view_authpermission'),
(93, 'Can add auth user', 24, 'add_authuser'),
(94, 'Can change auth user', 24, 'change_authuser'),
(95, 'Can delete auth user', 24, 'delete_authuser'),
(96, 'Can view auth user', 24, 'view_authuser'),
(97, 'Can add auth user groups', 25, 'add_authusergroups'),
(98, 'Can change auth user groups', 25, 'change_authusergroups'),
(99, 'Can delete auth user groups', 25, 'delete_authusergroups'),
(100, 'Can view auth user groups', 25, 'view_authusergroups'),
(101, 'Can add auth user user permissions', 26, 'add_authuseruserpermissions'),
(102, 'Can change auth user user permissions', 26, 'change_authuseruserpermissions'),
(103, 'Can delete auth user user permissions', 26, 'delete_authuseruserpermissions'),
(104, 'Can view auth user user permissions', 26, 'view_authuseruserpermissions'),
(105, 'Can add django admin log', 27, 'add_djangoadminlog'),
(106, 'Can change django admin log', 27, 'change_djangoadminlog'),
(107, 'Can delete django admin log', 27, 'delete_djangoadminlog'),
(108, 'Can view django admin log', 27, 'view_djangoadminlog'),
(109, 'Can add django content type', 28, 'add_djangocontenttype'),
(110, 'Can change django content type', 28, 'change_djangocontenttype'),
(111, 'Can delete django content type', 28, 'delete_djangocontenttype'),
(112, 'Can view django content type', 28, 'view_djangocontenttype'),
(113, 'Can add django migrations', 29, 'add_djangomigrations'),
(114, 'Can change django migrations', 29, 'change_djangomigrations'),
(115, 'Can delete django migrations', 29, 'delete_djangomigrations'),
(116, 'Can view django migrations', 29, 'view_djangomigrations'),
(117, 'Can add django session', 30, 'add_djangosession'),
(118, 'Can change django session', 30, 'change_djangosession'),
(119, 'Can delete django session', 30, 'delete_djangosession'),
(120, 'Can view django session', 30, 'view_djangosession'),
(121, 'Can add tipo alimento', 31, 'add_tipoalimento'),
(122, 'Can change tipo alimento', 31, 'change_tipoalimento'),
(123, 'Can delete tipo alimento', 31, 'delete_tipoalimento'),
(124, 'Can view tipo alimento', 31, 'view_tipoalimento'),
(125, 'Can add tipo descarte', 32, 'add_tipodescarte'),
(126, 'Can change tipo descarte', 32, 'change_tipodescarte'),
(127, 'Can delete tipo descarte', 32, 'delete_tipodescarte'),
(128, 'Can view tipo descarte', 32, 'view_tipodescarte'),
(129, 'Can add vacunas', 33, 'add_vacunas'),
(130, 'Can change vacunas', 33, 'change_vacunas'),
(131, 'Can delete vacunas', 33, 'delete_vacunas'),
(132, 'Can view vacunas', 33, 'view_vacunas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `documento` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `documento`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$Jx1x4wITKsrV7H3TdO4rTP$RdCt2z/oddcKyxFGlf3B/UZQOUuUjjzrxQlNJ3oy8Uk=', '2023-05-07 02:09:42.421056', 1, 'anderson', '', '', 12345, 'andersonordonez455@gmail.com', 1, 1, '2023-03-31 01:29:57.967445');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-03-31 02:43:29.544109', '1', 'TipoDoc object (1)', 1, '[{\"added\": {}}]', 18, 1),
(2, '2023-03-31 02:43:35.890606', '2', 'TipoDoc object (2)', 1, '[{\"added\": {}}]', 18, 1),
(3, '2023-03-31 02:47:31.799885', '1', 'Usuario object (1)', 1, '[{\"added\": {}}]', 20, 1),
(4, '2023-03-31 13:33:48.288426', '1', 'Usuario object (1)', 2, '[{\"changed\": {\"fields\": [\"Conexion\"]}}]', 20, 1),
(5, '2023-03-31 14:13:18.272897', '1', 'Usuario object (1)', 2, '[{\"changed\": {\"fields\": [\"Conexion\"]}}]', 20, 1),
(6, '2023-04-04 04:53:41.832824', '0', 'DetalleJornada object (0)', 1, '[{\"added\": {}}]', 8, 1),
(7, '2023-04-04 05:11:12.581075', '1', 'ProduccionDiaria object (1)', 1, '[{\"added\": {}}]', 16, 1),
(8, '2023-04-08 16:20:58.489863', '5', 'Yumbo', 2, '[]', 19, 1),
(19, '2023-05-24 15:53:21.481073', '17', 'asd', 2, '[{\"changed\": {\"fields\": [\"Is active\"]}}]', 20, 10),
(20, '2023-05-24 15:53:27.125269', '17', 'asd', 2, '[]', 20, 10),
(21, '2023-06-13 15:19:56.878064', '10', 'andersons', 2, '[{\"changed\": {\"fields\": [\"Nombre\"]}}]', 20, 16),
(22, '2023-06-13 15:20:45.715808', '10', 'anderson', 2, '[{\"changed\": {\"fields\": [\"Nombre\"]}}]', 20, 16),
(23, '2023-06-20 00:10:50.608727', '25', 'willingtom', 2, '[{\"changed\": {\"fields\": [\"Is staff\"]}}]', 20, 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'control', 'alimentacion'),
(21, 'control', 'authgroup'),
(22, 'control', 'authgrouppermissions'),
(23, 'control', 'authpermission'),
(24, 'control', 'authuser'),
(25, 'control', 'authusergroups'),
(26, 'control', 'authuseruserpermissions'),
(8, 'control', 'detallejornada'),
(27, 'control', 'djangoadminlog'),
(28, 'control', 'djangocontenttype'),
(29, 'control', 'djangomigrations'),
(30, 'control', 'djangosession'),
(9, 'control', 'estados'),
(10, 'control', 'ficha'),
(11, 'control', 'gallinas'),
(12, 'control', 'galpones'),
(13, 'control', 'jornada'),
(14, 'control', 'linea'),
(15, 'control', 'mortalidaddescarte'),
(16, 'control', 'producciondiaria'),
(17, 'control', 'rol'),
(31, 'control', 'tipoalimento'),
(32, 'control', 'tipodescarte'),
(18, 'control', 'tipodoc'),
(19, 'control', 'tiposhuevos'),
(20, 'control', 'usuario'),
(33, 'control', 'vacunas'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-03-30 22:38:25.436022'),
(2, 'auth', '0001_initial', '2023-03-30 22:38:25.715409'),
(3, 'admin', '0001_initial', '2023-03-30 22:38:25.776802'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-03-30 22:38:25.783804'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-03-30 22:38:25.789802'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-03-30 22:38:25.828306'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-03-30 22:38:25.859260'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-03-30 22:38:25.889326'),
(9, 'auth', '0004_alter_user_username_opts', '2023-03-30 22:38:25.896326'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-03-30 22:38:25.920325'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-03-30 22:38:25.923328'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-03-30 22:38:25.929329'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-03-30 22:38:25.940357'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-03-30 22:38:25.951331'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-03-30 22:38:25.982329'),
(16, 'auth', '0011_update_proxy_permissions', '2023-03-30 22:38:25.988361'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-03-30 22:38:25.999328'),
(18, 'control', '0001_initial', '2023-03-30 22:38:26.010326'),
(19, 'sessions', '0001_initial', '2023-03-30 22:38:26.030797'),
(20, 'control', '0002_alter_usuario_options', '2023-04-04 02:57:24.766597'),
(21, 'control', '0003_alter_jornada_options', '2023-04-11 17:54:04.223436'),
(22, 'control', '0004_alter_gallinas_options', '2023-05-20 20:21:24.827495'),
(23, 'control', '0005_alter_usuario_options', '2023-05-20 23:36:04.428722'),
(24, 'control', '0006_authgroup_authgrouppermissions_authpermission_and_more', '2023-05-24 15:52:30.656910'),
(25, 'control', '0007_tipoalimento', '2023-05-25 02:50:06.781807'),
(26, 'control', '0008_tipodescarte_vacunas', '2023-07-10 20:25:48.507204');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('04luvslnct2dsphtgqmlg3xafpgbdwcn', '.eJxVjEEOwiAQRe_C2pAOGQq4dO8ZCMMMUjU0Ke3KeHdt0oVu_3vvv1RM21rj1mWJE6uzAqdOvyOl_JC2E76ndpt1ntu6TKR3RR-06-vM8rwc7t9BTb1-6yBjKk4wAABZNwiOQq4IogML3oEnQlMMch44CBMCeGQTwFoma9X7AwFjN7A:1qTmh6:vx1P_hLb0V-nyQ3B_pUZ4eaLTuoUd87FvB9zNOOd67A', '2023-08-23 17:10:00.973361'),
('1l31c24dmvc3bpar2nroahnqh7qwuld2', '.eJxVjEEOwiAQRe_C2pAOGQq4dO8ZCMMMUjU0Ke3KeHdt0oVu_3vvv1RM21rj1mWJE6uzAqdOvyOl_JC2E76ndpt1ntu6TKR3RR-06-vM8rwc7t9BTb1-6yBjKk4wAABZNwiOQq4IogML3oEnQlMMch44CBMCeGQTwFoma9X7AwFjN7A:1q7MY0:fPcg18mQQ_1JuZJ4nWqeGrL3aGFH7ScB2H77Vw-tUKo', '2023-06-22 20:47:56.161817'),
('1pr2a73fpdvxxfa9e41vof8et7mqcogy', '.eJxVjEEOwiAURO_C2hDg8ym4dO8ZCPBBqoYmpV0Z764kXehuMu_NvJgP-1b93vPqZ2JnJtnpt4shPXIbgO6h3Raelratc-RD4Qft_LpQfl4O9--ghl6_a5MnQxaCkE6SiKVYjXkihaQBCKxFNHakKJBULNFpcJQsSm0UGMfeH88FNvc:1plB3o:dQBHhLE2kUuf48dAcbi_ef_WNpKTBfDLfqNjdS-XRn8', '2023-04-22 16:05:04.794440'),
('30yhlimgnj0jag8pdn4z6sn6wb4x65ma', '.eJxVjEEOwiAQRe_C2pDCwNS6dO8ZCDMDUjU0Ke3KeHfbpAvd_vfef6sQ16WEtaU5jKIuyqA6_Y4U-ZnqTuQR633SPNVlHknvij5o07dJ0ut6uH8HJbay1R1FceAxEZtsejC2dzkTIaO1HgDYCvthINis6OHsfEfG2IyYE4pVny8CbjeU:1qAh8j:SZTj1arvvLvHO0uvUSrm9IpwnFyKBkSESnVhea7Ighc', '2023-07-02 01:23:37.268022'),
('7sztzrsset0uk6bcua024vry2j9it73l', '.eJxVjMsOwiAQRf-FtSFAO8zg0r3fQHhMpWogKe3K-O_apAvd3nPOfQkftrX4rfPi5yzOwozi9DvGkB5cd5Lvod6aTK2uyxzlrsiDdnltmZ-Xw_07KKGXb03MxoRpMEQKDNOULKE2WQPrcRgyWmIiixoVYbToEgSnEyt0AAhOvD_mUja3:1qsxzK:YdRbAXLv3Y9Er20DqEGBcFlcfphoc25k99EtOJpyDkY', '2023-11-01 04:16:54.060502'),
('blq7evc9fn049k2uehoia3n972j0nqh7', '.eJxVjEEOwiAQRe_C2hBoxwFcuu8ZyNAZbNVAUtqV8e7apAvd_vfef6lI2zrFrckSZ1YXZVGdfsdE40PKTvhO5Vb1WMu6zEnvij5o00NleV4P9-9gojZ9a3JEIaM4IemdyQDkDYgwejxDAIuEGWzITsCD7TkBd9ibLliXGEb1_gAWFDfn:1qvOG1:LEjYEHKz6S9NsOLOyyGG16gaM3wzoQutzqX10G2RDrg', '2023-11-07 20:44:09.001724'),
('cpssqmo4ihhxtx59ee3nzqk74gqbl7vz', '.eJxVjMEOwiAQRP-FsyFQuuB69O43EFgWqRpISnsy_rtt0oMmc5r3Zt7Ch3Upfu08-ymJi9BWnH7LGOjJdSfpEeq9SWp1macod0UetMtbS_y6Hu7fQQm9bGujCQhYWYYEWmFWCsdMOBAak6MOqCxZiudBWccAo3bEuAWYEJ0Wny_62je6:1q95sP:gereQB1ilf6rJNgUa-B-6LUfoU1RPwrlBf7UGFsad3M', '2023-06-27 15:24:09.315381'),
('gqvoqqw6foro74sru6a0wi7x43dno9y9', '.eJxVjEEOwiAQRe_C2pDCwNS6dO8ZCDMDUjU0Ke3KeHfbpAvd_vfef6sQ16WEtaU5jKIuyqA6_Y4U-ZnqTuQR633SPNVlHknvij5o07dJ0ut6uH8HJbay1R1FceAxEZtsejC2dzkTIaO1HgDYCvthINis6OHsfEfG2IyYE4pVny8CbjeU:1qOisk:6Y1hLfGM-AgN19Gi2EaEOhHEkOg-JZPyUIQEiPocmi8', '2023-08-09 18:05:06.187496'),
('jlqja5iy483acatvk6skhdaa05oc5t33', '.eJxVjEEOwiAURO_C2hDg8ym4dO8ZCPBBqoYmpV0Z764kXehuMu_NvJgP-1b93vPqZ2JnJtnpt4shPXIbgO6h3Raelratc-RD4Qft_LpQfl4O9--ghl6_a5MnQxaCkE6SiKVYjXkihaQBCKxFNHakKJBULNFpcJQsSm0UGMfeH88FNvc:1pi3am:j60Mjegf6R_LeayHmWQYOn6e1Nnx320FPkjfQfALe6w', '2023-04-14 01:30:12.427000'),
('k7903ugpdtjy95xeqmnwhpxqufy40j26', '.eJxVjMEOwiAQRP-FsyFQuuB69O43EFgWqRpISnsy_rtt0oMmc5r3Zt7Ch3Upfu08-ymJi9BWnH7LGOjJdSfpEeq9SWp1macod0UetMtbS_y6Hu7fQQm9bGujCQhYWYYEWmFWCsdMOBAak6MOqCxZiudBWccAo3bEuAWYEJ0Wny_62je6:1q8iV4:egi-IXRnH7drIDNs60yKKagS5jpsaK6KO9-ZLvpygLU', '2023-06-26 14:26:30.813778'),
('kf120es5d3020yfunng1b0vc8mz1yd96', '.eJxVjEEOwiAQRe_C2pDCwNS6dO8ZCDMDUjU0Ke3KeHfbpAvd_vfef6sQ16WEtaU5jKIuyqA6_Y4U-ZnqTuQR633SPNVlHknvij5o07dJ0ut6uH8HJbay1R1FceAxEZtsejC2dzkTIaO1HgDYCvthINis6OHsfEfG2IyYE4pVny8CbjeU:1qf28u:uEzPIVRFiBmPWHLAjSgsAlNIiXpJGBHsW7MUCk9vlHM', '2023-09-23 17:53:12.048363'),
('o11ivm2f3nm8stkx6s08gki1xxo3jbfm', '.eJxVjEEOwiAQRe_C2pDCwNS6dO8ZCDMDUjU0Ke3KeHfbpAvd_vfef6sQ16WEtaU5jKIuyqA6_Y4U-ZnqTuQR633SPNVlHknvij5o07dJ0ut6uH8HJbay1R1FceAxEZtsejC2dzkTIaO1HgDYCvthINis6OHsfEfG2IyYE4pVny8CbjeU:1qBl6H:MZkqwlv7cvemHg9b-iXhXwgfW0ojA9v3PSEXwfIoW2g', '2023-07-04 23:49:29.127899'),
('oapynbdx3ad455iomkfuyp2mthkgpd6f', 'eyJfcGFzc3dvcmRfcmVzZXRfdG9rZW4iOiJicTFtZzQtYWJiZTJjZjU1YjU0NWFmZTM2MTRiMTAwOWZjOTBlZGIifQ:1qBJVs:GlS6lj88w2ZkbFVtWnWKmssCcofunyDU_HZyG5FlYPg', '2023-07-03 18:22:04.302487'),
('rmd1iemfishjvab34wq68hqq107rtp4s', '.eJxVjEEOwiAQRe_C2pDCwNS6dO8ZCDMDUjU0Ke3KeHfbpAvd_vfef6sQ16WEtaU5jKIuyqA6_Y4U-ZnqTuQR633SPNVlHknvij5o07dJ0ut6uH8HJbay1R1FceAxEZtsejC2dzkTIaO1HgDYCvthINis6OHsfEfG2IyYE4pVny8CbjeU:1qiKKW:VgW_CsnZfea2Efl0slM2oJqpk3APGMjNETqXcdu2nxE', '2023-10-02 19:54:48.486715'),
('syrlohsebsnfgn4le50eyhr5idoly9c2', '.eJxVjEEOwiAQRe_C2pDCwNS6dO8ZCDMDUjU0Ke3KeHfbpAvd_vfef6sQ16WEtaU5jKIuyqA6_Y4U-ZnqTuQR633SPNVlHknvij5o07dJ0ut6uH8HJbay1R1FceAxEZtsejC2dzkTIaO1HgDYCvthINis6OHsfEfG2IyYE4pVny8CbjeU:1qsvYh:vui1jWN-pCAciaMHDkC6K5-A6LGFs5V527v8C0u6sbo', '2023-11-01 01:41:15.429571'),
('tzeykgz5k5zrlrvcevr51yp8e9mt0kdd', '.eJxVjEEOwiAQRe_C2pAOGQq4dO8ZCMMMUjU0Ke3KeHdt0oVu_3vvv1RM21rj1mWJE6uzAqdOvyOl_JC2E76ndpt1ntu6TKR3RR-06-vM8rwc7t9BTb1-6yBjKk4wAABZNwiOQq4IogML3oEnQlMMch44CBMCeGQTwFoma9X7AwFjN7A:1q20rH:NXqbaej-jiQXAk4-iyJ5zyGvKC8-XrcWjAz73Nr_5Cs', '2023-06-08 02:37:43.789857'),
('xench5hpouq42o7hl13uyoeyay44298z', '.eJxVjMEOwiAQRP-FsyFQuuB69O43EFgWqRpISnsy_rtt0oMmc5r3Zt7Ch3Upfu08-ymJi9BWnH7LGOjJdSfpEeq9SWp1macod0UetMtbS_y6Hu7fQQm9bGujCQhYWYYEWmFWCsdMOBAak6MOqCxZiudBWccAo3bEuAWYEJ0Wny_62je6:1qAcoT:MmUx1TiVvEDIjk5nn99X26W2-zLeN-6xJ_n6bHu5ovM', '2023-07-01 20:46:25.038293'),
('zfsxvccpsa0ho21v1n4voiq4s2mh2g2t', '.eJxVjEEOwiAQRe_C2pDCwNS6dO8ZCDMDUjU0Ke3KeHfbpAvd_vfef6sQ16WEtaU5jKIuyqA6_Y4U-ZnqTuQR633SPNVlHknvij5o07dJ0ut6uH8HJbay1R1FceAxEZtsejC2dzkTIaO1HgDYCvthINis6OHsfEfG2IyYE4pVny8CbjeU:1qBLKJ:iKy6zbuhjEMS-VAY_gkulrqi2neaHyCEVQV1vTWNLvY', '2023-07-03 20:18:15.657740');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados`
--

CREATE TABLE IF NOT EXISTS `estados` (
  `estado` int(2) NOT NULL AUTO_INCREMENT,
  `descrip` varchar(30) NOT NULL,
  PRIMARY KEY (`estado`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estados`
--

INSERT INTO `estados` (`estado`, `descrip`) VALUES
(1, 'Inactivo(a)'),
(2, 'Activo(a)');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ficha`
--

CREATE TABLE IF NOT EXISTS `ficha` (
  `id_ficha` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_regis` date NOT NULL,
  `num_ficha` varchar(50) NOT NULL,
  `titulacion` varchar(50) NOT NULL,
  `estado_ficha` int(2) NOT NULL,
  PRIMARY KEY (`id_ficha`),
  KEY `estado_ficha` (`estado_ficha`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ficha`
--

INSERT INTO `ficha` (`id_ficha`, `fecha_regis`, `num_ficha`, `titulacion`, `estado_ficha`) VALUES
(1, '2023-03-28', '2540092', 'ADSO', 1),
(4, '2023-04-22', '1232354', 'ASDasd', 1),
(5, '2023-04-22', '1232354', 'ASDasd', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gallinas`
--

CREATE TABLE IF NOT EXISTS `gallinas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_galpon` int(11) NOT NULL,
  `id_linea` int(11) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `cantidad_gallinas` int(11) NOT NULL,
  `peso_promedio` int(11) NOT NULL,
  `edad_sem` int(11) NOT NULL,
  `procedencia` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_linea` (`id_linea`),
  KEY `id_galpon` (`id_galpon`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gallinas`
--

INSERT INTO `gallinas` (`id`, `id_galpon`, `id_linea`, `fecha_ingreso`, `cantidad_gallinas`, `peso_promedio`, `edad_sem`, `procedencia`) VALUES
(26, 4, 1, '2023-04-29', 23, 23, 23, 'asdasdas'),
(29, 4, 1, '2023-07-10', 32, 54, 65, 'sfc'),
(30, 4, 1, '2023-08-04', 23, 23, 12, 'asd'),
(31, 4, 1, '2023-08-11', 23, 12, 23, 'asdsd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `galpones`
--

CREATE TABLE IF NOT EXISTS `galpones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `nombre_galpon` varchar(100) NOT NULL,
  `ancho` int(11) NOT NULL,
  `largo` int(11) NOT NULL,
  `area` int(11) NOT NULL,
  `capac_bebed` int(11) NOT NULL,
  `cant_bebed` int(11) NOT NULL,
  `capac_comed` int(11) NOT NULL,
  `cant_comed` int(11) NOT NULL,
  `capac_gall` int(11) NOT NULL,
  `cant_gall` int(11) NOT NULL,
  `capac_nidales` int(11) NOT NULL,
  `cant_nidales` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `galpones`
--

INSERT INTO `galpones` (`id`, `fecha`, `nombre_galpon`, `ancho`, `largo`, `area`, `capac_bebed`, `cant_bebed`, `capac_comed`, `cant_comed`, `capac_gall`, `cant_gall`, `capac_nidales`, `cant_nidales`) VALUES
(4, '2023-04-26', 'Galpon 2', 11, 11, 121, 32, 32, 32, 32, 32, 32, 32, 32);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jornada`
--

CREATE TABLE IF NOT EXISTS `jornada` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jornada` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `jornada`
--

INSERT INTO `jornada` (`id`, `jornada`) VALUES
(1, 'Mañana'),
(2, 'Mediodia'),
(3, 'Tarde');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `linea`
--

CREATE TABLE IF NOT EXISTS `linea` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `linea`
--

INSERT INTO `linea` (`id`, `nombre`) VALUES
(1, 'HLB');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mortalidad_descarte`
--

CREATE TABLE IF NOT EXISTS `mortalidad_descarte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `id_galpon` int(11) NOT NULL,
  `cant_muertas` int(11) DEFAULT NULL,
  `cant_descarte` int(11) DEFAULT NULL,
  `id_tipo_descarte` int(11) DEFAULT NULL,
  `saldo` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_galpon` (`id_galpon`),
  KEY `id_detalle_descarte` (`id_tipo_descarte`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mortalidad_descarte`
--

INSERT INTO `mortalidad_descarte` (`id`, `fecha`, `id_galpon`, `cant_muertas`, `cant_descarte`, `id_tipo_descarte`, `saldo`) VALUES
(4, '2023-04-30', 4, 23, 34, 1, 21),
(7, '2023-08-23', 4, 12, 123, 1, 103),
(8, '2023-10-23', 4, 123, 123, 1, 123);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `produccion_diaria`
--

CREATE TABLE IF NOT EXISTS `produccion_diaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_galpon` int(11) NOT NULL,
  `id_jornada` int(11) NOT NULL,
  `id_tipo_huevo` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `rotos` int(11) NOT NULL,
  `descarte` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_detalle_jornada` (`id_tipo_huevo`),
  KEY `id_tipo_huevo` (`id_tipo_huevo`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_galpon` (`id_galpon`,`id_jornada`),
  KEY `id_jornada` (`id_jornada`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `produccion_diaria`
--

INSERT INTO `produccion_diaria` (`id`, `id_galpon`, `id_jornada`, `id_tipo_huevo`, `cantidad`, `rotos`, `descarte`, `id_usuario`, `fecha`) VALUES
(2, 4, 1, 3, 23, 23, 4234, 1, '0000-00-00'),
(3, 4, 2, 4, 23, 2, 231, 1, '0000-00-00'),
(4, 4, 3, 4, 23, 123, 342, 1, '0000-00-00'),
(5, 4, 2, 4, 23, 123, 123, 1, '0000-00-00'),
(9, 4, 1, 2, 12312, 34, 23, 1, '2023-06-13'),
(11, 4, 2, 5, 2, 23, 12, 17, '2023-06-18'),
(12, 4, 2, 1, 23, 23, 12, 1, '2023-04-22'),
(13, 4, 3, 1, 123, 12312, 123, 1, '2023-04-22'),
(14, 4, 2, 2, 23, 12312, 1232, 16, '2023-04-24'),
(15, 4, 1, 2, 123, 123, 123, 16, '2023-10-17');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE IF NOT EXISTS `rol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_rol` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `tipo_rol`) VALUES
(1, 'Administrador'),
(2, 'Aprendiz');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_huevos`
--

CREATE TABLE IF NOT EXISTS `tipos_huevos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipos_huevos` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tipos_huevos`
--

INSERT INTO `tipos_huevos` (`id`, `tipos_huevos`) VALUES
(1, 'B'),
(2, 'A'),
(3, 'AA'),
(4, 'AAA'),
(5, 'Yumbo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_alimento`
--

CREATE TABLE IF NOT EXISTS `tipo_alimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_alimento`
--

INSERT INTO `tipo_alimento` (`id`, `nombre`) VALUES
(1, 'Prepostura'),
(2, 'Postura'),
(3, 'Levante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_descarte`
--

CREATE TABLE IF NOT EXISTS `tipo_descarte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_descarte`
--

INSERT INTO `tipo_descarte` (`id`, `tipo`) VALUES
(1, 'autodonacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_doc`
--

CREATE TABLE IF NOT EXISTS `tipo_doc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_doc` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_doc`
--

INSERT INTO `tipo_doc` (`id`, `tipo_doc`) VALUES
(1, 'Cedula de Ciudadanía (CC)'),
(2, 'Tarjeta de Identidad (TI)'),
(3, 'Cedula Extranjera (CE)'),
(4, 'Libreta Militar (LM)');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `is_superuser` tinyint(1) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `id_tipo_doc` int(11) DEFAULT NULL,
  `documento` varchar(10) NOT NULL,
  `celular` varchar(10) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `id_ficha` int(11) DEFAULT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  `imagen` varchar(60) DEFAULT NULL,
  `registro` date DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_ficha` (`id_ficha`,`id_rol`),
  KEY `id_tipo_doc` (`id_tipo_doc`),
  KEY `id_rol` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`is_superuser`, `id`, `nombre`, `apellido`, `id_tipo_doc`, `documento`, `celular`, `correo`, `id_ficha`, `id_rol`, `password`, `imagen`, `registro`, `last_login`, `is_active`, `is_staff`) VALUES
(0, 1, 'Anderson', 'Ordonez', 1, '1002966350', '3103494305', 'abc@algo.com', 1, 2, '123', '', '2023-03-31', '2023-07-14 18:52:09', 1, 0),
(0, 3, 'asd', 'asd', 1, 'asd', '123', 'asd@gmail.com1', 1, 1, 'asd', NULL, '2023-04-03', NULL, 0, 0),
(0, 4, 'asd', 'asd', 1, '1002966356', '123', 'abc@algo.com', 1, 1, '123', 'imagen_usuario/imagen.png', '2023-04-11', NULL, 0, 0),
(0, 5, 'asd', 'ad', 1, '123', '123', 'asd@gmail.com', 1, 2, '123', 'imagen_usuario/code.png', '2023-04-11', NULL, 0, 0),
(0, 6, 'asd', 'asd', 1, '123', '123', 'benicia1270@gmail.com', 1, 2, '123', 'imagen_usuario/imagen.png', '2023-04-11', NULL, 0, 0),
(0, 7, 'asd', 'asd', 1, '123', '123', 'abc@algo.com', 1, 2, '123', 'imagen_usuario/ejercicios_python.png', '2023-04-11', NULL, 0, 0),
(0, 9, 'sdf', 'sdf', 1, '12345', '3103494305', 'abc@algo.com', 1, 2, '123', 'imagen_usuario/imagen_KjGgyXk.png', '2023-05-20', NULL, 0, 0),
(1, 10, 'anderson', 'ordonez', 1, '123456', NULL, NULL, 1, 1, 'pbkdf2_sha256$390000$KkDi6pHfsW8SWzJELdyhc0$rBUWRvYM2Nr5N8TZBiMq4uQ79cFz6xqGIUHMZ98dpMM=', '', '2023-05-20', '2023-07-13 18:49:53', 1, 1),
(0, 11, 'asd', 'asd', 1, '1234', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$KkDi6pHfsW8SWzJELdyhc0$rBUWRvYM2Nr5N8TZBiMq4uQ79cFz6xqGIUHMZ98dpMM=', '', '2023-05-20', NULL, 0, 0),
(0, 12, 'asd', 'asd', 1, '789', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$7ULfk5JP29eG2O0m8EjMyh$qcDwlhT6h6Z4EBgMP5zTXu0//56Nhe4aRHs7Y/6oYB8=', 'imagen_usuario/imagen_H7zAHh5.png', '2023-05-20', '2023-05-20 23:29:59', 1, 0),
(0, 15, 'asd', 'asd', 1, '456', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$ey6Eivf5aF7oZgIfgznVtW$QmNMBlFeQG/ByMHCxnHxAio4ee1A5kzvQW8zpZ5oNNs=', '', '2023-05-20', NULL, 0, 0),
(1, 16, 'Anderson', 'asd', 1, '001', '3103494306', 'abc@algo.com', 1, 1, 'pbkdf2_sha256$600000$h0wlTjL0rcMPZcODNcoJov$I8H4lkV9mJ39Ri2VhNjWYgbrru/CXUsRywiPMeCUH7Y=', 'imagen_usuario/Nitro_Wallpaper_01_3840x2400.jpg', '2023-05-20', '2023-10-24 20:44:08', 1, 1),
(0, 17, 'asd', 'asd', 1, '002', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$600000$wqRpPkO1Z3s9RptfjmbBB7$C+tG93ibb1yjRZDeNtEYC/xI7zjmHUko+qQkv65cGgw=', 'imagen_usuario/Free_Sample_By_Wix_PYkQcED.jpg', '2023-05-24', '2023-10-24 04:17:28', 1, 0),
(0, 18, 'asd', 'asd', 1, '003', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$pddMibRppC1OS5Xw1hzR6a$WOlLsbw0OvJRe4jh5mngzjUJfX4hicoNcG7RfRjUqDQ=', '', '2023-05-24', '2023-06-19 21:45:21', 1, 0),
(0, 19, 'asd', 'asd', 1, '004', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$b6H1g0wSkHMOLT2vXnjjoy$Yip/U5p2EFSyu38dX8WY9fdhRA1Ns3/zdl7LA5vVOxA=', 'imagen_usuario/Free_Sample_By_Wix_wXnw55w.jpg', '2023-05-24', '2023-05-24 16:06:49', 1, 0),
(0, 20, 'sdf', 'sdf', 1, '005', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$b6H1g0wSkHMOLT2vXnjjoy$Yip/U5p2EFSyu38dX8WY9fdhRA1Ns3/zdl7LA5vVOxA=', 'imagen_usuario/Free_Sample_By_Wix_DetwenE.jpg', '2023-05-24', '2023-06-12 23:23:00', 1, 0),
(0, 21, 'asd', 'asd', 1, '006', '3103494305', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$b6H1g0wSkHMOLT2vXnjjoy$Yip/U5p2EFSyu38dX8WY9fdhRA1Ns3/zdl7LA5vVOxA=', 'imagen_usuario/Free_Sample_By_Wix_7oq14c8.jpg', '2023-05-24', '2023-06-20 00:05:08', 1, 0),
(0, 22, 'Legal', 'asd', 1, '007', '3103494305', 'jaordonez653@misena.edu.co', 1, 2, 'pbkdf2_sha256$390000$IBAHgkKzGK4mrq93CcBvop$KRX8GX7cRZ/z4Xg0Pjr7g9UvNzFKz1QfFDaGvOOpeVg=', 'imagen_usuario/Free_Sample_By_Wix_RLTP8Nq.jpg', '2023-05-24', '2023-06-20 00:04:43', 1, 0),
(0, 23, 'asd', 'asd', 1, '013', '3103494305', 'andersonordonez455@gmail.co', 1, 1, 'pbkdf2_sha256$390000$nVzyhe4XDV3id34MqCsywo$SKZHPyvxyWZGweUh81aTzvDNQ4OHYPsMxyXyVbrLRbM=', 'imagen_usuario/ficha.png', '2023-06-12', '2023-06-19 23:51:52', 1, 1),
(0, 24, 'asd', 'asd', 1, '014', '3103494305', 'andersonordonez455@gmail.com', 1, 2, 'pbkdf2_sha256$600000$HcFlFskGUMC4bSB1TL7SqC$PVuDn2Ow2fbKT9adop2tWPQTU3/vz3ZdTghTO+8J0Wc=', 'imagen_usuario/jornada.png', '2023-06-14', '2023-10-18 04:33:44', 1, 0),
(0, 25, 'willingtom', 'ordoñez', 1, '1061779992', '3104046043', 'willybiker46@gmail.com', 1, 1, 'pbkdf2_sha256$390000$INeAC73J1sbqsiuULPUOXr$KJ2x31ast4BPy6x79uX+03BkfrY3QFx/2Di09Cul0f8=', 'imagen_usuario/cyberpunk_2077_Toyota_Supra_OvgCLwE.jpg', '2023-06-17', '2023-09-09 15:43:05', 1, 1),
(0, 26, 'Angie Catherine', 'Hoyos Velasco', 1, '1002968988', '3137228133', 'katehoyos21@gmail.com', 1, 2, 'pbkdf2_sha256$390000$lt1pbcdZRumSNRd1Zt0658$/lMmdBRKDEejZ7FGpo51H31F2fobOXvQCTlig1qgu9U=', 'imagen_usuario/images.jpeg', '2023-07-10', '2023-07-10 19:28:08', 1, 0),
(0, 27, 'asd', 'asd', 1, '123333', '123', NULL, 1, 2, 'pbkdf2_sha256$390000$KnwYpT11SiFCIRftqII5Jy$Bq+sdroVOIOBIXu6y0NmY5/tqOj4kIryxiiqHSf6Nf0=', 'imagen_usuario/Opera_Captura_de_pantalla_2023-07-25_150542_l', '2023-07-25', '2023-07-25 22:34:12', 1, 0),
(0, 28, 'Andrea', 'Trujillo', 1, '1060796022', '3128651728', 'trujillo.velasco.paola.andrea@gmail.com', 1, 2, 'pbkdf2_sha256$390000$HzZTz7K53lNAzfXMcK4HXf$ecXXnvjxU7FG519t18JY25UWBTZ0/HIPJnwD6wOJH8I=', 'imagen_usuario/16942735972656592605156669010403.jpg', '2023-09-09', '2023-09-09 15:33:34', 1, 0),
(0, 29, 'asd', 'aasd', 1, '111', '123', 'abc@algo.com', 1, 2, 'pbkdf2_sha256$390000$5lCBAosZ1EAXKgwjiYbJ1p$uShn+XiPvlwPqc7JudYSzWtCmUcOw4GDduyxBTKlLAM=', '', '2023-09-09', '2023-09-09 17:47:01', 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacunas`
--

CREATE TABLE IF NOT EXISTS `vacunas` (
  `Idvacunas` int(5) NOT NULL AUTO_INCREMENT,
  `Nombrev` varchar(60) NOT NULL,
  `Presentacion` varchar(60) NOT NULL,
  PRIMARY KEY (`Idvacunas`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vacunas`
--

INSERT INTO `vacunas` (`Idvacunas`, `Nombrev`, `Presentacion`) VALUES
(1, 'hUEVOTONOL', 'Ampolla 5 cm'),
(2, 'MAREK', 'AMPOLLETA POR 5Ml'),
(3, 'COCCIDIA', 'FRASCO POR 1000 DOSIS'),
(4, 'SALMONELLA', 'FRASCO POR 100 DOSIS'),
(5, 'BRONQUITIS', 'FRASCO POR 1000 DOSIS'),
(6, 'MYCOPLASMA', 'TARRO POR 50 Ml'),
(7, 'PASTEURELLA', 'TARRO POR 250 ML'),
(8, 'ENCEFALOMIELITIS', 'FRASCO PARA 1000 DOSIS'),
(9, 'VIRUELA', 'FRASCO 2Ml /100dosis'),
(10, 'HEPATITIS', 'TARRO 500Ml'),
(11, 'SINDROME DE BAJA POSTURA', 'TARRO DE 1000Ml / 1000 dosis');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alimentacion`
--
ALTER TABLE `alimentacion`
  ADD CONSTRAINT `alimentacion_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpones` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `alimentacion_ibfk_2` FOREIGN KEY (`id_tipo_alimento`) REFERENCES `tipo_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ficha`
--
ALTER TABLE `ficha`
  ADD CONSTRAINT `ficha_ibfk_1` FOREIGN KEY (`estado_ficha`) REFERENCES `estados` (`estado`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `gallinas`
--
ALTER TABLE `gallinas`
  ADD CONSTRAINT `gallinas_ibfk_2` FOREIGN KEY (`id_linea`) REFERENCES `linea` (`id`),
  ADD CONSTRAINT `gallinas_ibfk_3` FOREIGN KEY (`id_galpon`) REFERENCES `galpones` (`id`);

--
-- Filtros para la tabla `mortalidad_descarte`
--
ALTER TABLE `mortalidad_descarte`
  ADD CONSTRAINT `mortalidad_descarte_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpones` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `mortalidad_descarte_ibfk_2` FOREIGN KEY (`id_tipo_descarte`) REFERENCES `tipo_descarte` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `produccion_diaria`
--
ALTER TABLE `produccion_diaria`
  ADD CONSTRAINT `produccion_diaria_ibfk_2` FOREIGN KEY (`id_tipo_huevo`) REFERENCES `tipos_huevos` (`id`),
  ADD CONSTRAINT `produccion_diaria_ibfk_3` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `produccion_diaria_ibfk_4` FOREIGN KEY (`id_galpon`) REFERENCES `galpones` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `produccion_diaria_ibfk_5` FOREIGN KEY (`id_jornada`) REFERENCES `jornada` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_tipo_doc`) REFERENCES `tipo_doc` (`id`),
  ADD CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`id_ficha`) REFERENCES `ficha` (`id_ficha`),
  ADD CONSTRAINT `usuario_ibfk_3` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
