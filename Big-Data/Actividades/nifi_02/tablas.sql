-- Crear la base de datos
CREATE DATABASE CentroEstudios;

-- Seleccionar la base de datos a usar
USE CentroEstudios;

-- Crear la tabla de Actividades
CREATE TABLE Actividades (
    ID_Actividad VARCHAR(6),
    Descripción VARCHAR(35),
    Trimestre INTEGER,
    Peso INTEGER,
    Fecha_Ini DATE,
    Fecha_Fin DATE
);

-- Crear la tabla de Alumnos
CREATE TABLE Alumnos (
    ID_Alumno VARCHAR(5),
    Nombre VARCHAR(25),
    Apellido1 VARCHAR(25),
    Apellido2 VARCHAR(25),
    Grupo VARCHAR(10),
    Email VARCHAR(40)
);

-- Crear la tabla de Notas
CREATE TABLE Notas (
    ID_Alumno VARCHAR(5),
    ID_Actividad VARCHAR(6),
    Nota DOUBLE
);

-- Crear la tabla de Registro
CREATE TABLE Registro (
    Paso VARCHAR(255),
    Estado VARCHAR(50),
    Fecha_Hora TIMESTAMP
);
