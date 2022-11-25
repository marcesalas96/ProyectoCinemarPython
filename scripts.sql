-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Cinemar
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Cinemar
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Cinemar` DEFAULT CHARACTER SET utf8 ;
USE `Cinemar` ;

-- -----------------------------------------------------
-- Table `Cinemar`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cinemar`.`Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Edad` INT NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Cinemar`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cinemar`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `nombreUsuario` VARCHAR(45) NOT NULL,
  `clave` VARCHAR(45) NOT NULL,
  `tipoUsuario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsuario`),
  CONSTRAINT `idcliente`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `Cinemar`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Cinemar`.`Pelicula`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cinemar`.`Pelicula` (
  `Titulo` VARCHAR(45) NOT NULL,
  `Genero` VARCHAR(45) NOT NULL,
  `Duracion` TIME NOT NULL,
  `Descripcion` VARCHAR(180) NOT NULL,
  PRIMARY KEY (`Titulo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Cinemar`.`Sala`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cinemar`.`Sala` (
  `idSala` INT NOT NULL AUTO_INCREMENT,
  `Tipo` VARCHAR(45) NOT NULL,
  `Capacidad` INT NOT NULL,
  PRIMARY KEY (`idSala`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Cinemar`.`Funcion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cinemar`.`Funcion` (
  `idFuncion` INT NOT NULL AUTO_INCREMENT,
  `Pelicula` VARCHAR(45) NOT NULL,
  `Sala` INT NOT NULL,
  `Horario` TIME NOT NULL,
  `fechaInicio` DATE NOT NULL,
  PRIMARY KEY (`idFuncion`),
  INDEX `Titulo_idx` (`Pelicula` ASC) VISIBLE,
  INDEX `Sala_idx` (`Sala` ASC) VISIBLE,
  CONSTRAINT `Titulo`
    FOREIGN KEY (`Pelicula`)
    REFERENCES `Cinemar`.`Pelicula` (`Titulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Sala`
    FOREIGN KEY (`Sala`)
    REFERENCES `Cinemar`.`Sala` (`idSala`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Cinemar`.`Butaca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cinemar`.`Butaca` (
  `Sala` INT NOT NULL,
  `Fila` INT NOT NULL,
  `Columna` VARCHAR(1) NOT NULL,
  INDEX `idSala_idx` (`Sala` ASC) VISIBLE,
  CONSTRAINT `idSala`
    FOREIGN KEY (`Sala`)
    REFERENCES `Cinemar`.`Sala` (`idSala`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Cinemar`.`Reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cinemar`.`Reserva` (
  `idReserva` INT NOT NULL,
  `Funcion` INT NOT NULL,
  `Usuario` INT NOT NULL,
  `Butaca` INT NOT NULL,
  `Precio` DECIMAL(4) NOT NULL,
  PRIMARY KEY (`idReserva`),
  INDEX `filaButaca_idx` (`Butaca` ASC) VISIBLE,
  INDEX `usuario_idx` (`Usuario` ASC) VISIBLE,
  INDEX `funcion_idx` (`Funcion` ASC) VISIBLE,
  CONSTRAINT `filaButaca`
    FOREIGN KEY (`Butaca`)
    REFERENCES `Cinemar`.`Butaca` (`Sala`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `columnaButaca`
    FOREIGN KEY (`Butaca`)
    REFERENCES `Cinemar`.`Butaca` (`Sala`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `usuario`
    FOREIGN KEY (`Usuario`)
    REFERENCES `Cinemar`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `funcion`
    FOREIGN KEY (`Funcion`)
    REFERENCES `Cinemar`.`Funcion` (`idFuncion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
