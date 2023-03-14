CREATE DATABASE /*IF NOT EXISTS*/ `lib`;

USE `lib`;

/* Data for Members */

CREATE TABLE `Members` (
  `Membership ID` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Faculty` varchar(255) NOT NULL,
  `Phone` int NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Borrowable` int DEFAULT '2',
  `Reservable` int DEFAULT '2',
  PRIMARY KEY (`Membership ID`),
  UNIQUE KEY `Membership ID` (`Membership ID`),
  UNIQUE KEY `Phone` (`Phone`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* Data for Book Details */

CREATE TABLE `Book Details` (
  `ISBN` varchar(255) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `Author_1` varchar(255) NOT NULL,
  `Author_2` varchar(255) NOT NULL,
  `Author_3` varchar(255) NOT NULL,
  `Publisher` varchar(255) NOT NULL,
  `Publication Year` int NOT NULL,
  PRIMARY KEY (`ISBN`),
  UNIQUE KEY `ISBN` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* Data for each individual Book */

CREATE TABLE `Books` (
  `Accession Number` varchar(255) NOT NULL,
  `ISBN` varchar(255) NOT NULL,
  PRIMARY KEY (`Accession Number`),
  UNIQUE KEY `Accession Number` (`Accession Number`),
  KEY `ISBN` (`ISBN`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `Book Details` (`ISBN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* Data for Book Loans */

CREATE TABLE `Book Loan` (
  `Loan ID` int NOT NULL AUTO_INCREMENT,
  `Membership ID` varchar(255) NOT NULL,
  `Borrow Date` date NOT NULL,
  `Due Date` date NOT NULL,
  `Return Date` date DEFAULT NULL,
  `Accession Number` varchar(255) NOT NULL,
  PRIMARY KEY (`Loan ID`),
  KEY `Membership ID` (`Membership ID`),
  KEY `Accession Number` (`Accession Number`),
  CONSTRAINT `book loan_ibfk_1` FOREIGN KEY (`Membership ID`) REFERENCES `Members` (`Membership ID`),
  CONSTRAINT `book loan_ibfk_2` FOREIGN KEY (`Accession Number`) REFERENCES `Books` (`Accession Number`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* Data for Book Reservations */

CREATE TABLE `Book Reservation` (
  `Reservation ID` int NOT NULL AUTO_INCREMENT,
  `Accession Number` varchar(255) NOT NULL,
  `Membership ID` varchar(255) NOT NULL,
  `Reserve Date` date NOT NULL,
  PRIMARY KEY (`Reservation ID`),
  UNIQUE KEY `Accession Number` (`Accession Number`),
  KEY `Membership ID` (`Membership ID`),
  CONSTRAINT `book reservation_ibfk_1` FOREIGN KEY (`Accession Number`) REFERENCES `Books` (`Accession Number`),
  CONSTRAINT `book reservation_ibfk_2` FOREIGN KEY (`Membership ID`) REFERENCES `Members` (`Membership ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* Data for Outstanding Fines */

CREATE TABLE `Outstanding Fine` (
  `Fine ID` int NOT NULL AUTO_INCREMENT,
  `Membership ID` varchar(255) NOT NULL,
  `Fine Amount` float NOT NULL,
  PRIMARY KEY (`Fine ID`),
  UNIQUE KEY `Membership ID` (`Membership ID`),
  CONSTRAINT `outstanding fine_ibfk_1` FOREIGN KEY (`Membership ID`) REFERENCES `Members` (`Membership ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* Data for Fine Payment Records */

CREATE TABLE `Fine Payment` (
  `Payment ID` int NOT NULL AUTO_INCREMENT,
  `Membership ID` varchar(255) NOT NULL,
  `Payment Amount` float NOT NULL,
  `Payment Date` date NOT NULL,
  PRIMARY KEY (`Payment ID`),
  KEY `Membership ID` (`Membership ID`),
  CONSTRAINT `fine payment_ibfk_1` FOREIGN KEY (`Membership ID`) REFERENCES `Members` (`Membership ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
