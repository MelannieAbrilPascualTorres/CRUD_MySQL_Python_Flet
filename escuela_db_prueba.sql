CREATE DATABASE IF NOT EXISTS escuela_db;
USE escuela_db;

CREATE TABLE alumnos (
    matricula VARCHAR(20) PRIMARY KEY,
    apellido_paterno VARCHAR(50) NOT NULL,
    apellido_materno VARCHAR(50) NOT NULL,
    nombres VARCHAR(100) NOT NULL,
    curp VARCHAR(18) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefono CHAR(10) NOT NULL,
    ciudad_origen VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    disciplina VARCHAR(100) NOT NULL,
    foto VARCHAR(255)
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO alumnos (
    matricula,
    apellido_paterno,
    apellido_materno,
    nombres,
    curp,
    especialidad,
    telefono,
    ciudad_origen,
    estado,
    disciplina,
    foto
)
VALUES
(
    'A001',
    'Ramirez',
    'Ortiz',
    'Sofia',
    'RAOS050315MCHMRFA1',
    'Programación',
    '6141234567',
    'Chihuahua',
    'Chihuahua',
    'Voleibol',
    'c:\Users\hmoon\Downloads\prueba.png'
),
(
    'A002',
    'Lopez',
    'Martinez',
    'Carlos',
    'LOMC040720HCHPRBA2',
    'Electrónica',
    '6149876543',
    'Delicias',
    'Chihuahua',
    'Fútbol',
    'c:\Users\hmoon\Downloads\prueba.png'
);
INSERT INTO usuarios (usuario, password)
VALUES (
    'Melannie',
    '$2b$12$.NRoZCN1kOSFWPPxk3vng.FUboI.uKxjc8yAKDbWSlY8Z3jWqtxfW'
);