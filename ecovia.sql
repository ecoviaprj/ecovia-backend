-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: ecovia
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `animals`
--

DROP TABLE IF EXISTS `animals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `cost_trees` int DEFAULT '0',
  `cost_coins` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animals`
--

LOCK TABLES `animals` WRITE;
/*!40000 ALTER TABLE `animals` DISABLE KEYS */;
INSERT INTO `animals` VALUES (1,'Tiger',50,0),(2,'Elephant',0,100),(3,'Panda',100,0),(4,'Kangaroo',0,200);
/*!40000 ALTER TABLE `animals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `challenge_master`
--

DROP TABLE IF EXISTS `challenge_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `challenge_master` (
  `id` int NOT NULL AUTO_INCREMENT,
  `challenge_text` text NOT NULL,
  `option_a` varchar(100) NOT NULL,
  `option_b` varchar(100) NOT NULL,
  `option_c` varchar(100) NOT NULL,
  `option_d` varchar(100) NOT NULL,
  `correct_answer` char(1) NOT NULL,
  `date` date NOT NULL,
  `trees_awarded` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `challenge_master`
--

LOCK TABLES `challenge_master` WRITE;
/*!40000 ALTER TABLE `challenge_master` DISABLE KEYS */;
INSERT INTO `challenge_master` VALUES (1,'What is the process by which plants make food?','Photosynthesis','Respiration','Transpiration','Germination','A','2025-08-01',7),(2,'Which gas is essential for human survival?','Nitrogen','Carbon Monoxide','Oxygen','Hydrogen','C','2025-08-02',5),(3,'Which layer of the Earth’s atmosphere contains the ozone layer?','Troposphere','Stratosphere','Mesosphere','Exosphere','B','2025-08-03',10),(4,'What does \'zero waste\' mean?','Recycle everything','Produce no waste','Burn all waste','Compost only','B','2025-08-04',10),(5,'What causes acid rain?','Ozone','CO2','Sulfur & nitrogen oxides','Chlorine','C','2025-08-05',7),(6,'Which of these is a sustainable fishing method?','Bottom trawling','Cyanide fishing','Pole and line','Drift netting','C','2025-08-06',5),(7,'Which continent has the largest forest cover?','Asia','Africa','Europe','South America','D','2025-08-07',5),(8,'What day is celebrated as World Environment Day?','June 5','April 22','March 21','July 1','A','2025-08-08',10),(9,'What is the main cause of ocean acidification?','Plastic','Oil spills','CO2 absorption','Overfishing','C','2025-08-09',7),(10,'Which country generates most of its electricity from geothermal sources?','Iceland','India','China','Nigeria','A','2025-08-10',7),(11,'What is the term for animals active during night?','Carnivore','Diurnal','Herbivore','Nocturnal','D','2025-08-11',5),(12,'What tree is known as the \'lungs of the planet\'?','Oak','Pine','Amazon rainforest','Banyan','C','2025-08-12',7),(13,'What does \'biodegradable\' mean?','Can’t be broken down','Breaks down naturally','Made by machines','Not recyclable','B','2025-08-13',7),(14,'Which material is worst for the ocean?','Wood','Paper','Plastic','Glass','C','2025-08-14',5),(15,'What is the term for growing plants without soil?','Hydroponics','Bioplastics','Cultivation','Xeriscaping','A','2025-08-15',10),(16,'What renewable energy uses sunlight?','Wind','Hydro','Solar','Tidal','C','2025-08-16',7),(17,'What’s an example of green transport?','Private car','Electric bus','Motorbike','Helicopter','B','2025-08-17',10),(18,'What is the hottest year on record globally (as of 2023)?','1998','2016','2020','2023','D','2025-08-18',7),(19,'Coral bleaching is caused by?','Overfishing','Pollution','Rising sea temperatures','Mining','C','2025-08-19',7),(20,'What country banned single-use plastic in 2019?','USA','Rwanda','Brazil','Australia','B','2025-08-20',5),(21,'What is the symbol of recycling?','Triangle','Heart','Recycle bin','Three chasing arrows','D','2025-08-21',7),(22,'Which farming practice is most sustainable?','Monoculture','Slash & burn','Organic farming','Chemical intensive','C','2025-08-22',10),(23,'Which species is a pollinator?','Mosquito','Butterfly','Lizard','Rat','B','2025-08-23',5),(24,'Which of these reduces carbon footprint the most?','Walking','Taking car','Flying','Eating beef','A','2025-08-24',10),(25,'What is a green building?','Painted green','Uses less energy','Made of plastic','Built on mountains','B','2025-08-25',5),(26,'Why are wetlands important?','Store garbage','Breed mosquitoes','Act as natural filters','No benefit','C','2025-08-26',7),(27,'Which is a fast-renewable resource?','Plastic','Bamboo','Petrol','Coal','B','2025-08-27',7),(28,'What causes global warming?','Volcanoes','Deforestation','Recycling','Earthquakes','B','2025-08-28',5),(29,'Which is the best way to save water?','Wash car daily','Fix leaky taps','Overwater lawns','Use sprinklers','B','2025-08-29',10),(30,'What do trees absorb from the atmosphere?','Methane','Nitrogen','Carbon Dioxide','Oxygen','C','2025-08-30',5);
/*!40000 ALTER TABLE `challenge_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_challenges`
--

DROP TABLE IF EXISTS `daily_challenges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_challenges` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `challenge_id` int NOT NULL,
  `user_answer` char(1) DEFAULT NULL,
  `is_correct` tinyint(1) DEFAULT '0',
  `completed` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `challenge_id` (`challenge_id`),
  CONSTRAINT `daily_challenges_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `daily_challenges_ibfk_2` FOREIGN KEY (`challenge_id`) REFERENCES `challenge_master` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_challenges`
--

LOCK TABLES `daily_challenges` WRITE;
/*!40000 ALTER TABLE `daily_challenges` DISABLE KEYS */;
INSERT INTO `daily_challenges` VALUES (1,1,9,'c',1,1),(2,1,10,'a',1,1);
/*!40000 ALTER TABLE `daily_challenges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eco_actions`
--

DROP TABLE IF EXISTS `eco_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eco_actions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text,
  `eco_coins` int DEFAULT '0',
  `level` int DEFAULT '1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eco_actions`
--

LOCK TABLES `eco_actions` WRITE;
/*!40000 ALTER TABLE `eco_actions` DISABLE KEYS */;
INSERT INTO `eco_actions` VALUES (1,'Avoid using Plastics','Use biodegradable products instead of non-biodegradable products like plastic bottles,polythene covers,etc.',100,1,'2025-08-01 00:00:00'),(2,'Plant a Tree','Plant a sapling in your neighborhood or campus to improve greenery.',200,2,'2025-08-01 00:00:00'),(3,'Organize Clean-Up Drive','Lead or participate in a community clean-up to remove waste from nature spots.',300,3,'2025-08-01 00:00:00');
/*!40000 ALTER TABLE `eco_actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eco_tasks`
--

DROP TABLE IF EXISTS `eco_tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eco_tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `task_id` varchar(255) DEFAULT NULL,
  `task_name` varchar(255) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `status` enum('pending','verified','rejected') DEFAULT 'pending',
  `date_assigned` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `eco_tasks_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eco_tasks`
--

LOCK TABLES `eco_tasks` WRITE;
/*!40000 ALTER TABLE `eco_tasks` DISABLE KEYS */;
INSERT INTO `eco_tasks` VALUES (1,1,'1','Avoid using Plastics','D:/GIFTY COLLEGE/project/ecoverse-backend/static/uploads/c.jpg','rejected','2025-08-10'),(2,NULL,'1','Avoid using Plastics','D:/GIFTY COLLEGE/project/ecoverse-backend/static/uploads/soil.jpg','verified','2025-08-10');
/*!40000 ALTER TABLE `eco_tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leaderboard`
--

DROP TABLE IF EXISTS `leaderboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leaderboard` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `score` int DEFAULT '0',
  `completed_all` tinyint(1) DEFAULT '0',
  `completed_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `leaderboard_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leaderboard`
--

LOCK TABLES `leaderboard` WRITE;
/*!40000 ALTER TABLE `leaderboard` DISABLE KEYS */;
INSERT INTO `leaderboard` VALUES (1,1,22,0,'2025-08-09 02:42:37');
/*!40000 ALTER TABLE `leaderboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_animals`
--

DROP TABLE IF EXISTS `user_animals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_animals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `animal_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `animal_id` (`animal_id`),
  CONSTRAINT `user_animals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_animals_ibfk_2` FOREIGN KEY (`animal_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_animals`
--

LOCK TABLES `user_animals` WRITE;
/*!40000 ALTER TABLE `user_animals` DISABLE KEYS */;
INSERT INTO `user_animals` VALUES (1,1,2),(2,1,4);
/*!40000 ALTER TABLE `user_animals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `avatar_name` varchar(255) DEFAULT NULL,
  `total_trees` int DEFAULT '0',
  `total_eco_coins` int DEFAULT '0',
  `onboarding_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Alice','Miss Golden Glow',14,1200,'2025-07-29 16:08:06');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-10 11:46:14
