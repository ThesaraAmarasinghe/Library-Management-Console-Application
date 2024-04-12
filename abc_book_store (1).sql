-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2022 at 12:42 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `abc_book_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `BookNo` int(10) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `SubjectCode` int(20) NOT NULL,
  `Author` varchar(30) DEFAULT NULL,
  `Publisher` varchar(30) DEFAULT NULL,
  `Price` float NOT NULL,
  `Location` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`BookNo`, `Title`, `SubjectCode`, `Author`, `Publisher`, `Price`, `Location`) VALUES
(1, 'Dancer', 1, 'Colum  McCann', 'Picador Modern Classics', 1200, '2nd isle'),
(1001, 'Columbine', 2, 'Dave Cullen', 'Twelve', 1700, '4th row'),
(1819, 'Calf', 5, 'Andrea Kleine', 'Soft Skull', 1500.99, '4th row'),
(2101, 'Atonement', 4, 'Ian McEwan', 'Jonathan Cape', 2300, '2nd isle'),
(3101, 'Clockers', 6, 'Richard Price', 'Houghton Mifflin', 2500, '3rd row'),
(12345, 'Emma', 1, 'Jane Austen', 'John Murray', 3500, '1st row'),
(54321, 'Macbeth', 3, 'William Shakespeare', 'Edward Blount', 2500.5, '2nd isle');

-- --------------------------------------------------------

--
-- Table structure for table `chapter`
--

CREATE TABLE `chapter` (
  `BookNo` int(10) NOT NULL,
  `ChapterNo` int(5) NOT NULL,
  `ChapterTitle` varchar(30) DEFAULT NULL,
  `StartingPgNo` int(5) DEFAULT NULL,
  `EndingPgNo` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chapter`
--

INSERT INTO `chapter` (`BookNo`, `ChapterNo`, `ChapterTitle`, `StartingPgNo`, `EndingPgNo`) VALUES
(12345, 1, 'Chapter 1', 2, 15),
(12345, 2, 'Chapter 2', 11, 22),
(54321, 3, 'New Chapter 3', 20, 31),
(1, 4, 'Life journey', 44, 53),
(1001, 1, 'Python', 12, 31);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `SubjectCode` int(10) NOT NULL,
  `Name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`SubjectCode`, `Name`) VALUES
(1, 'Fiction'),
(2, 'Romance'),
(3, 'Tragedy'),
(4, 'Domestic fiction'),
(5, 'Historical fiction'),
(6, 'Crime'),
(8, 'Non-fiction'),
(9, 'Biography'),
(10, 'Thriller');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`BookNo`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`SubjectCode`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
