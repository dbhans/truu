-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ScheduleMatrix
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ScheduleMatrix` ;

-- -----------------------------------------------------
-- Schema ScheduleMatrix
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ScheduleMatrix` DEFAULT CHARACTER SET utf8 ;
USE `ScheduleMatrix` ;

-- -----------------------------------------------------
-- Table `Cours`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Cours` ;

CREATE TABLE IF NOT EXISTS `Cours` (
  `idCours` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `code` VARCHAR(10) NULL,
  `Unit` VARCHAR(6) NULL,
  `NumberHours` INT NULL,
  `Description` MEDIUMTEXT NULL,
  `status` BIT(2) NULL,
  PRIMARY KEY (`idCours`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Classroom`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Classroom` ;

CREATE TABLE IF NOT EXISTS `Classroom` (
  `idClassroom` INT NOT NULL AUTO_INCREMENT,
  `Numberplace` VARCHAR(45) NULL,
  `Room` INT NULL,
  `status` BIT(2) NULL,
  `Classroomcol` VARCHAR(45) NULL,
  PRIMARY KEY (`idClassroom`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Programs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Programs` ;

CREATE TABLE IF NOT EXISTS `Programs` (
  `idPrograms` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Code` VARCHAR(45) NULL,
  `Description` VARCHAR(255) NULL,
  `Requierements` VARCHAR(45) NULL,
  `status` BIT(2) NULL,
  `Cours_idCours` INT NOT NULL,
  PRIMARY KEY (`idPrograms`),
  CONSTRAINT `fk_Programs_Cours`
    FOREIGN KEY (`Cours_idCours`)
    REFERENCES `Cours` (`idCours`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Personnels`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Personnels` ;

CREATE TABLE IF NOT EXISTS `Personnels` (
  `idPersonnel` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(45) NULL,
  `lastName` VARCHAR(45) NULL,
  `personalEmail` VARCHAR(45) NULL,
  `emailMatrix` VARCHAR(45) NULL,
  `position` VARCHAR(45) NULL,
  `profession` VARCHAR(45) NULL,
  `note` VARCHAR(45) NULL,
  `status` BIT(2) NULL,
  `code` INT(6) NULL,
  PRIMARY KEY (`idPersonnel`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Availability`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Availability` ;

CREATE TABLE IF NOT EXISTS `Availability` (
  `idAvailability` INT NOT NULL AUTO_INCREMENT,
  `day` VARCHAR(45) NULL,
  `statTime` DATETIME NULL,
  `endTime` DATETIME NULL,
  `note` VARCHAR(45) NULL,
  `notavailable` BIT(2) NULL,
  `status` BIT(2) NULL,
  `Personnel_idPersonnel` INT NOT NULL,
  PRIMARY KEY (`idAvailability`),
  CONSTRAINT `fk_Availability_Personnel1`
    FOREIGN KEY (`Personnel_idPersonnel`)
    REFERENCES `Personnels` (`idPersonnel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `group` ;

CREATE TABLE IF NOT EXISTS `group` (
  `idgroup` INT NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `numberstudent` VARCHAR(45) NULL,
  `Starting` DATE NULL,
  `Ending` DATE NULL,
  `numberduration` INT NULL,
  `numbertime` VARCHAR(25) NULL,
  `status` BIT(2) NULL,
  `Created` DATETIME NULL,
  `Modified` DATETIME NULL,
  PRIMARY KEY (`idgroup`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Time`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Time` ;

CREATE TABLE IF NOT EXISTS `Time` (
  `idTime` INT NOT NULL AUTO_INCREMENT,
  `startTime` DATETIME NULL,
  `endTime` DATETIME NULL,
  PRIMARY KEY (`idTime`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Semesters`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Semesters` ;

CREATE TABLE IF NOT EXISTS `Semesters` (
  `idSemesters` INT NOT NULL AUTO_INCREMENT,
  `semester` VARCHAR(15) NULL,
  `startTime` DATETIME NULL,
  `endTime` DATETIME NULL,
  PRIMARY KEY (`idSemesters`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Schedule`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Schedule` ;

CREATE TABLE IF NOT EXISTS `Schedule` (
  `Classroom_idClassroom` INT NULL,
  `group_idgroup` INT NULL,
  `Personnel_idPersonnel` INT NULL,
  `Cours_idCours` INT NULL,
  `Time_idTime` INT NOT NULL,
  `Semesters_idSemesters` INT NOT NULL,
  `idSchedule` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idSchedule`),
  CONSTRAINT `fk_Classroom_has_group_Classroom1`
    FOREIGN KEY (`Classroom_idClassroom`)
    REFERENCES `Classroom` (`idClassroom`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Classroom_has_group_group1`
    FOREIGN KEY (`group_idgroup`)
    REFERENCES `group` (`idgroup`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Classroom_has_group_Personnel1`
    FOREIGN KEY (`Personnel_idPersonnel`)
    REFERENCES `Personnels` (`idPersonnel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Classroom_has_group_Cours1`
    FOREIGN KEY (`Cours_idCours`)
    REFERENCES `Cours` (`idCours`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Schedule_Time1`
    FOREIGN KEY (`Time_idTime`)
    REFERENCES `Time` (`idTime`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Schedule_Semesters1`
    FOREIGN KEY (`Semesters_idSemesters`)
    REFERENCES `Semesters` (`idSemesters`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Logs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Logs` ;

CREATE TABLE IF NOT EXISTS `Logs` (
  `idlog` INT NOT NULL AUTO_INCREMENT,
  `creation` DATETIME NULL,
  `modified` DATETIME NULL,
  `createdBy` INT NULL,
  `modifiedBy` INT NULL,
  `tableName` VARCHAR(45) NULL,
  `modifiedField` VARCHAR(45) NULL,
  `lastValue` VARCHAR(45) NULL,
  PRIMARY KEY (`idlog`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TeacherPreferences`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TeacherPreferences` ;

CREATE TABLE IF NOT EXISTS `TeacherPreferences` (
  `Personnels_idPersonnel` INT NOT NULL,
  `Cours_idCours` INT NOT NULL,
  `Note` VARCHAR(150) NULL,
  `rank` BIT(8) NULL,
  PRIMARY KEY (`Personnels_idPersonnel`, `Cours_idCours`),
  CONSTRAINT `fk_Personnels_has_Cours_Personnels1`
    FOREIGN KEY (`Personnels_idPersonnel`)
    REFERENCES `Personnels` (`idPersonnel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personnels_has_Cours_Cours1`
    FOREIGN KEY (`Cours_idCours`)
    REFERENCES `Cours` (`idCours`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AdminComments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `AdminComments` ;

CREATE TABLE IF NOT EXISTS `AdminComments` (
  `idAdminComments` INT NOT NULL AUTO_INCREMENT,
  `Comment` VARCHAR(255) NULL,
  PRIMARY KEY (`idAdminComments`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Softwares`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Softwares` ;

CREATE TABLE IF NOT EXISTS `Softwares` (
  `idSoftware` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Description` VARCHAR(45) NULL,
  `Type` VARCHAR(45) NULL,
  `Version` VARCHAR(45) NULL,
  PRIMARY KEY (`idSoftware`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Classroom_has_Softwares`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Classroom_has_Softwares` ;

CREATE TABLE IF NOT EXISTS `Classroom_has_Softwares` (
  `Classroom_idClassroom` INT NOT NULL,
  `Softwares_idSoftware` INT NOT NULL,
  PRIMARY KEY (`Classroom_idClassroom`, `Softwares_idSoftware`),
  CONSTRAINT `fk_Classroom_has_Softwares_Classroom1`
    FOREIGN KEY (`Classroom_idClassroom`)
    REFERENCES `Classroom` (`idClassroom`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Classroom_has_Softwares_Softwares1`
    FOREIGN KEY (`Softwares_idSoftware`)
    REFERENCES `Softwares` (`idSoftware`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
