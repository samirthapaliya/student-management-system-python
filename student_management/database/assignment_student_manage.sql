CREATE DATABASE  IF NOT EXISTS `assignment` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `assignment`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: assignment
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student_manage`
--

DROP TABLE IF EXISTS `student_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_manage` (
  `Student_Id` int NOT NULL,
  `First_name` varchar(100) DEFAULT NULL,
  `Last_name` varchar(100) DEFAULT NULL,
  `Gender` varchar(100) DEFAULT NULL,
  `Dob` varchar(100) DEFAULT NULL,
  `Contact` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Parent_name` varchar(100) DEFAULT NULL,
  `Parent_contact` varchar(45) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Student_Id`),
  UNIQUE KEY `Contact_UNIQUE` (`Contact`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `Parent_contact_UNIQUE` (`Parent_contact`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_manage`
--

LOCK TABLES `student_manage` WRITE;
/*!40000 ALTER TABLE `student_manage` DISABLE KEYS */;
INSERT INTO `student_manage` VALUES (31,'ram','thapa','Male','2-05-2000','9843158763','samthda@gmail.com','shyam','9841557963','ktm'),(32,'ram','thapa','Male','2-05-2000','9852145687','ramthapasha@gmail.com','hari','9632541025','ktm'),(34,'shankar','thapa','Male','2-05-2000','9852647895','shankarsh@gmail.com','shyam','9852461230','ktm'),(35,'ranjit','sharma','Male','2-05-2000','9845216985','ranjitsh@gmail.com','shyam','9836452784','ktm'),(52,'hari','Sharma','Male','2-05-2000','9852648925','harish@gmail.com','shyam','9823568415','ktm'),(53,'shyam','Sharma','Male','2-05-2000','9852641203','shyamsha@gmail.com','Ryam','9805264582','ktm');
/*!40000 ALTER TABLE `student_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-04 13:58:19
