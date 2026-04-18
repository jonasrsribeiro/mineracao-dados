CREATE DATABASE IF NOT EXISTS streaming;
USE streaming;

CREATE TABLE Generos (
    id_genero   INT PRIMARY KEY AUTO_INCREMENT,
    nome_genero VARCHAR(50) NOT NULL
);

CREATE TABLE Filmes (
    id_filme    INT PRIMARY KEY AUTO_INCREMENT,
    titulo      VARCHAR(150) NOT NULL,
    ano         YEAR NOT NULL,
    duracao_min INT NOT NULL,
    id_genero   INT NOT NULL,
    FOREIGN KEY (id_genero) REFERENCES Generos(id_genero)
);

CREATE TABLE Avaliacoes (
    id_avaliacao  INT PRIMARY KEY AUTO_INCREMENT,
    id_filme      INT NOT NULL,
    nome_usuario  VARCHAR(100) NOT NULL,
    nota          DECIMAL(3,1) NOT NULL CHECK (nota BETWEEN 0 AND 10),
    data_avaliacao DATE NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES Filmes(id_filme)
);

INSERT INTO Generos (nome_genero) VALUES
('Ação'),
('Comédia'),
('Drama'),
('Terror'),
('Ficção Científica');

INSERT INTO Filmes (titulo, ano, duracao_min, id_genero) VALUES
('Vingadores',         2012, 143, 1),
('Homem de Ferro',     2008, 126, 1),
('Se Beber Não Case',  2009, 100, 2),
('Todo Mundo em Pânico', 2000, 88, 2),
('O Poderoso Chefão',  1972, 175, 3),
('Forrest Gump',       1994, 142, 3),
('It - A Coisa',       2017, 135, 4),
('Invocação do Mal',   2013, 112, 4),
('Interestelar',       2014, 169, 5),
('Matrix',             1999, 136, 5);

INSERT INTO Avaliacoes (id_filme, nome_usuario, nota, data_avaliacao) VALUES
(1,  'Lucas',    9.0, '2026-01-05'),
(1,  'Mariana',  8.5, '2026-01-06'),
(1,  'Pedro',    7.0, '2026-01-07'),
(2,  'Lucas',    8.0, '2026-01-08'),
(2,  'Carla',    9.5, '2026-01-09'),
(3,  'Mariana',  7.5, '2026-01-10'),
(3,  'Pedro',    6.0, '2026-01-11'),
(4,  'Carla',    5.5, '2026-01-12'),
(5,  'Lucas',   10.0, '2026-01-13'),
(5,  'Mariana',  9.5, '2026-01-14'),
(6,  'Pedro',    9.0, '2026-01-15'),
(6,  'Carla',    8.5, '2026-01-16'),
(7,  'Lucas',    7.0, '2026-01-17'),
(7,  'Mariana',  8.0, '2026-01-18'),
(8,  'Pedro',    6.5, '2026-01-19'),
(9,  'Carla',    9.5, '2026-01-20'),
(9,  'Lucas',   10.0, '2026-01-21'),
(9,  'Mariana',  9.0, '2026-01-22'),
(10, 'Pedro',    8.5, '2026-01-23'),
(10, 'Carla',    9.0, '2026-01-24');
