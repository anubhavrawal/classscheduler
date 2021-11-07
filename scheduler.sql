-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: SCHEDULER
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add semester',1,'add_semester'),(2,'Can change semester',1,'change_semester'),(3,'Can delete semester',1,'delete_semester'),(4,'Can view semester',1,'view_semester'),(5,'Can add instructors',2,'add_instructors'),(6,'Can change instructors',2,'change_instructors'),(7,'Can delete instructors',2,'delete_instructors'),(8,'Can view instructors',2,'view_instructors'),(9,'Can add meeting_ times',3,'add_meeting_times'),(10,'Can change meeting_ times',3,'change_meeting_times'),(11,'Can delete meeting_ times',3,'delete_meeting_times'),(12,'Can view meeting_ times',3,'view_meeting_times'),(13,'Can add rooms',4,'add_rooms'),(14,'Can change rooms',4,'change_rooms'),(15,'Can delete rooms',4,'delete_rooms'),(16,'Can view rooms',4,'view_rooms'),(17,'Can add header_ map',5,'add_header_map'),(18,'Can change header_ map',5,'change_header_map'),(19,'Can delete header_ map',5,'delete_header_map'),(20,'Can view header_ map',5,'view_header_map'),(21,'Can add log entry',6,'add_logentry'),(22,'Can change log entry',6,'change_logentry'),(23,'Can delete log entry',6,'delete_logentry'),(24,'Can view log entry',6,'view_logentry'),(25,'Can add permission',7,'add_permission'),(26,'Can change permission',7,'change_permission'),(27,'Can delete permission',7,'delete_permission'),(28,'Can view permission',7,'view_permission'),(29,'Can add group',8,'add_group'),(30,'Can change group',8,'change_group'),(31,'Can delete group',8,'delete_group'),(32,'Can view group',8,'view_group'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add content type',10,'add_contenttype'),(38,'Can change content type',10,'change_contenttype'),(39,'Can delete content type',10,'delete_contenttype'),(40,'Can view content type',10,'view_contenttype'),(41,'Can add session',11,'add_session'),(42,'Can change session',11,'change_session'),(43,'Can delete session',11,'delete_session'),(44,'Can view session',11,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'admin','logentry'),(8,'auth','group'),(7,'auth','permission'),(9,'auth','user'),(10,'contenttypes','contenttype'),(5,'scheduler','header_map'),(2,'scheduler','instructors'),(3,'scheduler','meeting_times'),(4,'scheduler','rooms'),(1,'scheduler','semester'),(11,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-11-01 03:33:00.460397'),(2,'auth','0001_initial','2021-11-01 03:33:01.443980'),(3,'admin','0001_initial','2021-11-01 03:33:01.656107'),(4,'admin','0002_logentry_remove_auto_add','2021-11-01 03:33:01.667711'),(5,'admin','0003_logentry_add_action_flag_choices','2021-11-01 03:33:01.679653'),(6,'contenttypes','0002_remove_content_type_name','2021-11-01 03:33:01.833910'),(7,'auth','0002_alter_permission_name_max_length','2021-11-01 03:33:01.965537'),(8,'auth','0003_alter_user_email_max_length','2021-11-01 03:33:01.999717'),(9,'auth','0004_alter_user_username_opts','2021-11-01 03:33:02.011052'),(10,'auth','0005_alter_user_last_login_null','2021-11-01 03:33:02.092071'),(11,'auth','0006_require_contenttypes_0002','2021-11-01 03:33:02.097675'),(12,'auth','0007_alter_validators_add_error_messages','2021-11-01 03:33:02.116848'),(13,'auth','0008_alter_user_username_max_length','2021-11-01 03:33:02.214186'),(14,'auth','0009_alter_user_last_name_max_length','2021-11-01 03:33:02.304487'),(15,'auth','0010_alter_group_name_max_length','2021-11-01 03:33:02.333625'),(16,'auth','0011_update_proxy_permissions','2021-11-01 03:33:02.346967'),(17,'auth','0012_alter_user_first_name_max_length','2021-11-01 03:33:02.444528'),(18,'scheduler','0001_initial','2021-11-01 03:33:02.508728'),(19,'scheduler','0002_alter_semester_crn','2021-11-01 03:33:02.548094'),(20,'scheduler','0003_instructors_meeting_times_rooms','2021-11-01 03:33:02.671741'),(21,'scheduler','0004_auto_20211012_1957','2021-11-01 03:33:02.765536'),(22,'scheduler','0005_auto_20211024_1418','2021-11-01 03:33:02.775968'),(23,'scheduler','0005_auto_20211017_1536','2021-11-01 03:33:02.862990'),(24,'scheduler','0006_merge_0005_auto_20211017_1536_0005_auto_20211024_1418','2021-11-01 03:33:02.871222'),(25,'scheduler','0007_auto_20211024_1154','2021-11-01 03:33:02.945939'),(26,'scheduler','0008_auto_20211024_2002','2021-11-01 03:33:03.061227'),(27,'scheduler','0009_auto_20211026_1508','2021-11-01 03:33:03.356043'),(28,'scheduler','0010_auto_20211026_1534','2021-11-01 03:33:03.423761'),(29,'sessions','0001_initial','2021-11-01 03:33:03.490340');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheduler_header_map`
--

DROP TABLE IF EXISTS `scheduler_header_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduler_header_map` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `PageName` varchar(32) NOT NULL,
  `CSVheader` varchar(32) NOT NULL,
  `DBheader` varchar(32) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduler_header_map`
--

LOCK TABLES `scheduler_header_map` WRITE;
/*!40000 ALTER TABLE `scheduler_header_map` DISABLE KEYS */;
INSERT INTO `scheduler_header_map` VALUES (1,'scheduler_rooms','Room#','room_num','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(2,'scheduler_rooms','Room Type','room_type','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(3,'scheduler_rooms','Building','building','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(4,'scheduler_rooms','Campus','campus','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(5,'scheduler_rooms','Capacity','capacity','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(6,'scheduler_rooms','Room#','room_num','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(7,'scheduler_rooms','Room Type','room_type','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(8,'scheduler_rooms','Building','building','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(9,'scheduler_rooms','Campus','campus','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000'),(10,'scheduler_rooms','Capacity','capacity','0000-00-00 00:00:00.000000','0000-00-00 00:00:00.000000');
/*!40000 ALTER TABLE `scheduler_header_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheduler_instructors`
--

DROP TABLE IF EXISTS `scheduler_instructors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduler_instructors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_name` longtext NOT NULL,
  `first_name` longtext NOT NULL,
  `status` varchar(2) NOT NULL,
  `department` varchar(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduler_instructors`
--

LOCK TABLES `scheduler_instructors` WRITE;
/*!40000 ALTER TABLE `scheduler_instructors` DISABLE KEYS */;
INSERT INTO `scheduler_instructors` VALUES (1,'Al-Mawee','Wassnaa','F','cs'),(2,'Bhattacharjee','Shameek','F','cs'),(3,'Carr','Steve','F','cs'),(4,'de Doncker','Elise','F','cs'),(5,'Fong','Alvis','F','cs'),(6,'Hong','Guan Yue','F','cs'),(7,'Johnson','Jason','F','cs'),(8,'MacCreery','Colin','F','cs'),(9,'Rhodes','James','F','cs'),(10,'Shen','Wuwei','F','cs'),(11,'Yang','Li','F','cs'),(12,'Gupta','Ajay','F','CS'),(14,'Default','Default','F','CS');
/*!40000 ALTER TABLE `scheduler_instructors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheduler_meeting_times`
--

DROP TABLE IF EXISTS `scheduler_meeting_times`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduler_meeting_times` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `days` varchar(8) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=493 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduler_meeting_times`
--

LOCK TABLES `scheduler_meeting_times` WRITE;
/*!40000 ALTER TABLE `scheduler_meeting_times` DISABLE KEYS */;
INSERT INTO `scheduler_meeting_times` VALUES (1,'08:30:00.000000','09:20:00.000000','M'),(2,'08:30:00.000000','09:20:00.000000','MW'),(3,'08:30:00.000000','09:20:00.000000','MWF'),(4,'08:30:00.000000','09:20:00.000000','R'),(5,'08:30:00.000000','09:45:00.000000','TR'),(6,'08:30:00.000000','10:20:00.000000','MW'),(7,'08:30:00.000000','10:20:00.000000','T'),(8,'08:30:00.000000','10:20:00.000000','W'),(9,'08:30:00.000000','11:00:00.000000','TR'),(10,'08:30:00.000000','11:20:00.000000','F'),(11,'08:30:00.000000','11:20:00.000000','M'),(12,'08:30:00.000000','11:20:00.000000','R'),(13,'08:30:00.000000','11:20:00.000000','T'),(14,'08:30:00.000000','11:20:00.000000','TR'),(15,'08:30:00.000000','11:20:00.000000','W'),(16,'09:00:00.000000','09:50:00.000000','MWF'),(17,'09:00:00.000000','10:15:00.000000','M'),(18,'09:00:00.000000','10:15:00.000000','MW'),(19,'09:00:00.000000','10:15:00.000000','W'),(20,'09:00:00.000000','11:30:00.000000','MW'),(21,'09:30:00.000000','10:20:00.000000','M'),(22,'09:30:00.000000','10:20:00.000000','MW'),(23,'09:30:00.000000','10:20:00.000000','MWF'),(24,'09:30:00.000000','10:20:00.000000','TR'),(25,'09:30:00.000000','10:20:00.000000','W'),(26,'09:30:00.000000','10:45:00.000000','M'),(27,'09:30:00.000000','10:45:00.000000','MW'),(28,'09:30:00.000000','10:45:00.000000','TR'),(29,'09:30:00.000000','11:10:00.000000','MW'),(30,'09:30:00.000000','11:10:00.000000','R'),(31,'09:30:00.000000','11:10:00.000000','TR'),(32,'09:30:00.000000','11:20:00.000000','F'),(33,'09:30:00.000000','11:20:00.000000','R'),(34,'09:30:00.000000','11:20:00.000000','T'),(35,'09:30:00.000000','11:20:00.000000','TR'),(36,'09:30:00.000000','12:00:00.000000','MW'),(37,'09:30:00.000000','12:00:00.000000','R'),(38,'09:30:00.000000','12:00:00.000000','TR'),(39,'09:30:00.000000','12:20:00.000000','TR'),(40,'09:30:00.000000','12:50:00.000000','MW'),(41,'10:00:00.000000','11:15:00.000000','MW'),(42,'10:00:00.000000','11:15:00.000000','R'),(43,'10:00:00.000000','11:15:00.000000','T'),(44,'10:00:00.000000','11:15:00.000000','TR'),(45,'10:00:00.000000','12:50:00.000000','MW'),(46,'10:00:00.000000','13:00:00.000000','TR'),(47,'10:30:00.000000','11:20:00.000000','M'),(48,'10:30:00.000000','11:20:00.000000','MF'),(49,'10:30:00.000000','11:20:00.000000','MW'),(50,'10:30:00.000000','11:20:00.000000','TR'),(51,'10:30:00.000000','11:20:00.000000','TWRF'),(52,'10:30:00.000000','11:45:00.000000','MW'),(53,'10:30:00.000000','12:10:00.000000','M'),(54,'10:30:00.000000','12:10:00.000000','MW'),(55,'10:30:00.000000','12:10:00.000000','T'),(56,'10:30:00.000000','12:10:00.000000','TR'),(57,'10:30:00.000000','12:10:00.000000','W'),(58,'10:30:00.000000','12:20:00.000000','M'),(59,'10:30:00.000000','12:20:00.000000','T'),(60,'10:30:00.000000','12:20:00.000000','W'),(61,'10:30:00.000000','12:50:00.000000','TR'),(62,'10:30:00.000000','13:00:00.000000','R'),(63,'10:30:00.000000','13:20:00.000000','F'),(64,'10:30:00.000000','13:20:00.000000','T'),(65,'10:30:00.000000','15:20:00.000000','MW'),(66,'11:00:00.000000','12:15:00.000000','TR'),(67,'11:00:00.000000','12:15:00.000000','W'),(68,'11:30:00.000000','02:00:00.000000','R'),(69,'11:30:00.000000','12:20:00.000000','MW'),(70,'11:30:00.000000','12:20:00.000000','TR'),(71,'11:30:00.000000','12:40:00.000000','W'),(72,'11:30:00.000000','12:45:00.000000','MW'),(73,'11:30:00.000000','12:45:00.000000','R'),(74,'11:30:00.000000','12:45:00.000000','T'),(75,'11:30:00.000000','12:45:00.000000','TR'),(76,'11:30:00.000000','13:10:00.000000','R'),(77,'11:30:00.000000','13:10:00.000000','TR'),(78,'11:30:00.000000','13:20:00.000000','M'),(79,'11:30:00.000000','13:20:00.000000','R'),(80,'11:30:00.000000','13:20:00.000000','T'),(81,'11:30:00.000000','13:20:00.000000','W'),(82,'11:30:00.000000','14:00:00.000000','R'),(83,'11:30:00.000000','14:20:00.000000','F'),(84,'11:30:00.000000','14:20:00.000000','R'),(85,'11:30:00.000000','14:20:00.000000','T'),(86,'11:30:00.000000','14:20:00.000000','W'),(87,'12:00:00.000000','12:50:00.000000','F'),(88,'12:30:00.000000','13:20:00.000000','MW'),(89,'12:30:00.000000','13:45:00.000000','MW'),(90,'12:30:00.000000','13:45:00.000000','R'),(91,'12:30:00.000000','13:45:00.000000','W'),(92,'12:30:00.000000','14:10:00.000000','MW'),(93,'12:30:00.000000','14:10:00.000000','T'),(94,'12:30:00.000000','14:10:00.000000','TR'),(95,'12:30:00.000000','14:20:00.000000','F'),(96,'12:30:00.000000','14:20:00.000000','M'),(97,'12:30:00.000000','14:20:00.000000','T'),(98,'12:30:00.000000','14:20:00.000000','W'),(99,'12:30:00.000000','15:20:00.000000','F'),(100,'12:30:00.000000','15:20:00.000000','MW'),(101,'12:30:00.000000','15:20:00.000000','R'),(102,'12:30:00.000000','15:20:00.000000','T'),(103,'12:30:00.000000','15:20:00.000000','W'),(104,'13:00:00.000000','14:10:00.000000','W'),(105,'13:00:00.000000','14:15:00.000000','MW'),(106,'13:00:00.000000','14:15:00.000000','R'),(107,'13:00:00.000000','14:15:00.000000','TR'),(108,'13:00:00.000000','15:20:00.000000','TR'),(109,'13:00:00.000000','15:30:00.000000','R'),(110,'13:00:00.000000','15:40:00.000000','TR'),(111,'13:30:00.000000','14:20:00.000000','M'),(112,'13:30:00.000000','14:20:00.000000','MW'),(113,'13:30:00.000000','14:20:00.000000','MWF'),(114,'13:30:00.000000','14:45:00.000000','TR'),(115,'13:30:00.000000','15:10:00.000000','MW'),(116,'13:30:00.000000','15:20:00.000000','TR'),(117,'13:30:00.000000','15:20:00.000000','W'),(118,'13:30:00.000000','15:40:00.000000','MW'),(119,'13:30:00.000000','16:00:00.000000','MW'),(120,'13:30:00.000000','16:20:00.000000','F'),(121,'13:30:00.000000','16:20:00.000000','T'),(122,'13:30:00.000000','16:20:00.000000','TR'),(123,'14:00:00.000000','14:50:00.000000','F'),(124,'14:30:00.000000','15:20:00.000000','MW'),(125,'14:30:00.000000','15:20:00.000000','TR'),(126,'14:30:00.000000','15:20:00.000000','W'),(127,'14:30:00.000000','15:45:00.000000','M'),(128,'14:30:00.000000','15:45:00.000000','MW'),(129,'14:30:00.000000','15:45:00.000000','TR'),(130,'14:30:00.000000','15:45:00.000000','W'),(131,'14:30:00.000000','16:10:00.000000','MW'),(132,'14:30:00.000000','16:10:00.000000','R'),(133,'14:30:00.000000','16:10:00.000000','T'),(134,'14:30:00.000000','16:20:00.000000','R'),(135,'14:30:00.000000','16:20:00.000000','T'),(136,'14:30:00.000000','16:20:00.000000','W'),(137,'14:30:00.000000','16:50:00.000000','R'),(138,'14:30:00.000000','17:00:00.000000','R'),(139,'14:30:00.000000','17:00:00.000000','T'),(140,'14:30:00.000000','17:20:00.000000','R'),(141,'14:30:00.000000','17:20:00.000000','T'),(142,'14:30:00.000000','17:20:00.000000','W'),(143,'14:30:00.000000','17:50:00.000000','MW'),(144,'15:00:00.000000','15:50:00.000000','F'),(145,'15:00:00.000000','16:15:00.000000','MW'),(146,'15:30:00.000000','16:20:00.000000','M'),(147,'15:30:00.000000','16:20:00.000000','MR'),(148,'15:30:00.000000','16:20:00.000000','MW'),(149,'15:30:00.000000','16:20:00.000000','MWF'),(150,'15:30:00.000000','16:20:00.000000','TR'),(151,'15:30:00.000000','16:20:00.000000','W'),(152,'15:30:00.000000','16:45:00.000000','MW'),(153,'15:30:00.000000','17:10:00.000000','MW'),(154,'15:30:00.000000','18:00:00.000000','MR'),(155,'15:30:00.000000','18:00:00.000000','MW'),(156,'15:30:00.000000','18:00:00.000000','R'),(157,'15:30:00.000000','18:00:00.000000','TR'),(158,'15:30:00.000000','18:20:00.000000','F'),(159,'15:30:00.000000','18:20:00.000000','M'),(160,'15:30:00.000000','18:20:00.000000','R'),(161,'15:30:00.000000','18:20:00.000000','T'),(162,'15:30:00.000000','18:20:00.000000','W'),(163,'15:50:00.000000','18:20:00.000000','T'),(164,'16:00:00.000000','17:15:00.000000','M'),(165,'16:00:00.000000','17:15:00.000000','MW'),(166,'16:00:00.000000','17:15:00.000000','R'),(167,'16:00:00.000000','17:15:00.000000','T'),(168,'16:00:00.000000','17:15:00.000000','TR'),(169,'16:00:00.000000','17:15:00.000000','W'),(170,'16:00:00.000000','17:45:00.000000','TR'),(171,'16:00:00.000000','18:20:00.000000','W'),(172,'16:00:00.000000','18:30:00.000000','F'),(173,'16:00:00.000000','18:30:00.000000','M'),(174,'16:00:00.000000','18:30:00.000000','TR'),(175,'16:00:00.000000','18:50:00.000000','T'),(176,'16:30:00.000000','17:20:00.000000','MTWR'),(177,'16:30:00.000000','17:20:00.000000','MW'),(178,'16:30:00.000000','17:45:00.000000','MW'),(179,'16:30:00.000000','17:45:00.000000','TR'),(180,'16:30:00.000000','18:10:00.000000','M'),(181,'16:30:00.000000','18:10:00.000000','MW'),(182,'16:30:00.000000','18:10:00.000000','R'),(183,'16:30:00.000000','18:10:00.000000','T'),(184,'16:30:00.000000','18:10:00.000000','TR'),(185,'16:30:00.000000','18:10:00.000000','W'),(186,'16:30:00.000000','18:20:00.000000','M'),(187,'16:30:00.000000','18:20:00.000000','MW'),(188,'16:30:00.000000','18:20:00.000000','R'),(189,'16:30:00.000000','18:20:00.000000','T'),(190,'16:30:00.000000','18:20:00.000000','W'),(191,'16:30:00.000000','19:00:00.000000','MW'),(192,'16:30:00.000000','19:00:00.000000','TR'),(193,'16:30:00.000000','19:50:00.000000','MW'),(194,'16:30:00.000000','19:50:00.000000','TR'),(195,'17:00:00.000000','18:15:00.000000','TR'),(196,'17:30:00.000000','18:20:00.000000','M'),(197,'17:30:00.000000','18:20:00.000000','MW'),(198,'17:30:00.000000','18:45:00.000000','M'),(199,'17:30:00.000000','18:45:00.000000','MW'),(200,'17:30:00.000000','18:45:00.000000','TR'),(201,'17:30:00.000000','18:45:00.000000','W'),(202,'17:30:00.000000','19:10:00.000000','T'),(203,'17:30:00.000000','19:20:00.000000','M'),(204,'17:30:00.000000','19:20:00.000000','R'),(205,'17:30:00.000000','19:20:00.000000','T'),(206,'17:30:00.000000','19:20:00.000000','W'),(207,'17:30:00.000000','20:00:00.000000','MR'),(208,'17:30:00.000000','20:00:00.000000','R'),(209,'17:30:00.000000','20:00:00.000000','T'),(210,'18:00:00.000000','19:15:00.000000','MW'),(211,'18:00:00.000000','19:15:00.000000','T'),(212,'18:00:00.000000','19:30:00.000000','M'),(213,'18:00:00.000000','20:30:00.000000','MW'),(214,'18:00:00.000000','20:30:00.000000','R'),(215,'18:00:00.000000','20:30:00.000000','T'),(216,'18:00:00.000000','20:30:00.000000','W'),(217,'18:30:00.000000','19:20:00.000000','M'),(218,'18:30:00.000000','19:20:00.000000','R'),(219,'18:30:00.000000','19:45:00.000000','MW'),(220,'18:30:00.000000','19:45:00.000000','TR'),(221,'18:30:00.000000','20:10:00.000000','M'),(222,'18:30:00.000000','20:10:00.000000','T'),(223,'18:30:00.000000','20:20:00.000000','M'),(224,'18:30:00.000000','20:20:00.000000','T'),(225,'18:30:00.000000','20:20:00.000000','W'),(226,'18:30:00.000000','21:00:00.000000','M'),(227,'18:30:00.000000','21:00:00.000000','R'),(228,'18:30:00.000000','21:00:00.000000','T'),(229,'18:30:00.000000','21:00:00.000000','W'),(230,'18:30:00.000000','21:20:00.000000','M'),(231,'18:30:00.000000','21:20:00.000000','MW'),(232,'18:30:00.000000','21:20:00.000000','R'),(233,'18:30:00.000000','21:20:00.000000','T'),(234,'18:30:00.000000','21:20:00.000000','W'),(235,'19:00:00.000000','20:40:00.000000','MW'),(236,'19:00:00.000000','20:50:00.000000','T'),(237,'19:00:00.000000','21:00:00.000000','R'),(238,'19:00:00.000000','21:30:00.000000','T'),(239,'19:00:00.000000','21:50:00.000000','M'),(240,'19:00:00.000000','21:50:00.000000','R'),(241,'19:00:00.000000','21:50:00.000000','TR'),(242,'19:30:00.000000','21:20:00.000000','R'),(243,'19:30:00.000000','21:20:00.000000','T'),(244,'19:30:00.000000','21:20:00.000000','W'),(245,'19:30:00.000000','21:50:00.000000','M'),(247,'08:00:00.000000','10:50:00.000000','F');
/*!40000 ALTER TABLE `scheduler_meeting_times` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheduler_rooms`
--

DROP TABLE IF EXISTS `scheduler_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduler_rooms` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `campus` longtext NOT NULL,
  `building` longtext NOT NULL,
  `room_num` longtext NOT NULL,
  `capacity` int NOT NULL,
  `room_type` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduler_rooms`
--

LOCK TABLES `scheduler_rooms` WRITE;
/*!40000 ALTER TABLE `scheduler_rooms` DISABLE KEYS */;
INSERT INTO `scheduler_rooms` VALUES (1,'Parkview','Floyd','B122',10,'B'),(2,'Parkview','Floyd','F115',10,'B'),(3,'Parkview','Floyd','G113',10,'B'),(4,'Parkview','Floyd','A213',10,'B'),(5,'Parkview','Floyd','B211',10,'B'),(6,'Parkview','Floyd','F210',10,'B'),(7,'Parkview','Floyd','C208',24,'C'),(8,'Parkview','Floyd','C219',24,'C'),(9,'Parkview','Floyd','C220',26,'C'),(10,'Parkview','Floyd','C224',26,'C'),(11,'Parkview','Floyd','C226',28,'C'),(12,'Parkview','Floyd','C227',24,'C'),(13,'Parkview','Floyd','C228',24,'C'),(14,'Parkview','Floyd','C229',28,'C'),(15,'Parkview','Floyd','C122',36,'S'),(16,'Parkview','Floyd','C123',44,'S'),(17,'Parkview','Floyd','C124',36,'S'),(18,'Parkview','Floyd','C136',70,'S'),(19,'Parkview','Floyd','C141',32,'S'),(20,'Parkview','Floyd','D201',50,'S'),(21,'Parkview','Floyd','D202',38,'S'),(22,'Parkview','Floyd','D204A',36,'S'),(23,'Parkview','Floyd','D205',36,'S'),(24,'Parkview','Floyd','D206',30,'S'),(25,'Parkview','Floyd','D208',55,'S'),(26,'Parkview','Floyd','D210',40,'S'),(27,'Parkview','Floyd','D212',40,'S'),(28,'Parkview','Floyd','D109',150,'S'),(29,'Parkview','Floyd','D115',80,'S'),(30,'Parkview','Floyd','E121',25,'S'),(32,'Parkview','Floyd','A120',10,'B');
/*!40000 ALTER TABLE `scheduler_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheduler_semester`
--

DROP TABLE IF EXISTS `scheduler_semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduler_semester` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `crn` int NOT NULL,
  `dept` varchar(4) NOT NULL,
  `course_id` varchar(9) NOT NULL,
  `section` int NOT NULL,
  `status` varchar(1) NOT NULL,
  `title` longtext NOT NULL,
  `link1` varchar(2) NOT NULL,
  `link2` varchar(2) NOT NULL,
  `schedule_type` varchar(2) NOT NULL,
  `reserved` varchar(1) NOT NULL,
  `credit_hours` int NOT NULL,
  `billing_hours` int NOT NULL,
  `contact_hours` int NOT NULL,
  `grad_able` varchar(1) NOT NULL,
  `cap` int NOT NULL,
  `waitlist_cap` int NOT NULL,
  `spec_appr` varchar(5) NOT NULL,
  `meeting_type` varchar(5) NOT NULL,
  `begin_date` date NOT NULL,
  `end_date` date NOT NULL,
  `meet_time` int NOT NULL,
  `location` int NOT NULL,
  `site_code` varchar(5) NOT NULL,
  `primary_instructor` int NOT NULL,
  `fee` int NOT NULL,
  `comment` longtext NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scheduler_semester_crn_74b37f60_uniq` (`crn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduler_semester`
--

LOCK TABLES `scheduler_semester` WRITE;
/*!40000 ALTER TABLE `scheduler_semester` DISABLE KEYS */;
/*!40000 ALTER TABLE `scheduler_semester` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-01  0:28:08
