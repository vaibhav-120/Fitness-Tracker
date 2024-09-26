-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2024 at 03:56 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fitness_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `meals`
--

CREATE TABLE `meals` (
  `id` int(11) NOT NULL,
  `food` varchar(30) NOT NULL,
  `calories` int(11) NOT NULL,
  `fat` int(11) NOT NULL,
  `carbs` int(11) NOT NULL,
  `protein` int(11) NOT NULL,
  `mealtime` varchar(5) NOT NULL,
  `mealday` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `meals`
--

INSERT INTO `meals` (`id`, `food`, `calories`, `fat`, `carbs`, `protein`, `mealtime`, `mealday`) VALUES
(96, 'milk', 122, 5, 12, 8, 'b', '2024-01-25');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `height` float(11,5) NOT NULL,
  `weight` float(11,5) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `activity` varchar(30) NOT NULL,
  `weightgoal` int(11) NOT NULL,
  `timegoal` int(11) NOT NULL,
  `calorieperday` int(11) NOT NULL,
  `fatperday` int(11) NOT NULL,
  `carbsperday` int(11) NOT NULL,
  `proteinperday` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `username`, `password`, `age`, `height`, `weight`, `gender`, `activity`, `weightgoal`, `timegoal`, `calorieperday`, `fatperday`, `carbsperday`, `proteinperday`) VALUES
(97, 'vaibhav@gmail.com', 'test', 'test1234', 65, 1.42240, 56.00000, 'Male', 'Very Little', 49, 3, 816, 27, 102, 41);

-- --------------------------------------------------------

--
-- Table structure for table `weight_table`
--

CREATE TABLE `weight_table` (
  `id` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `weight_table`
--

INSERT INTO `weight_table` (`id`, `weight`, `date`) VALUES
(97, 56, '2024-01-25'),
(98, 80, '2024-02-05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email_2` (`email`,`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=98;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
