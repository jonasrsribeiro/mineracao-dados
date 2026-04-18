CREATE DATABASE IF NOT EXISTS empresa;
USE empresa;

CREATE TABLE Produtos (
    codigo_produto INT PRIMARY KEY,
    nome_produto   VARCHAR(100) NOT NULL,
    valor_produto  DECIMAL(10,2) NOT NULL
);

CREATE TABLE Clientes (
    codigo_cliente   INT PRIMARY KEY,
    nome_cliente     VARCHAR(100) NOT NULL,
    endereco_cliente VARCHAR(200)
);

CREATE TABLE Vendas (
    codigo_venda    INT PRIMARY KEY,
    codigo_cliente  INT NOT NULL,
    codigo_produto  INT NOT NULL,
    quantidade      INT NOT NULL,
    data_venda      DATE NOT NULL,
    FOREIGN KEY (codigo_cliente) REFERENCES Clientes(codigo_cliente),
    FOREIGN KEY (codigo_produto) REFERENCES Produtos(codigo_produto)
);

INSERT INTO Produtos VALUES
(1,  'Arroz',        20.00),
(2,  'Feijão',       15.00),
(3,  'Macarrão',     10.00),
(4,  'Pó de Café',   35.00),
(5,  'Sabão em Pó',  25.00),
(6,  'Suco',          7.00),
(7,  'Refrigerante',  9.00),
(8,  'Água Mineral',  3.00),
(9,  'Pão de Forma', 13.00),
(10, 'Shampoo',      30.00);

INSERT INTO Clientes VALUES
(1,  'Maria',    'Rua aaa'),
(2,  'Ana',      'Rua bbb'),
(3,  'Paula',    'Rua ccc'),
(4,  'Paulo',    'Rua ddd'),
(5,  'José',     'Rua eee'),
(6,  'João',     'Rua fff'),
(7,  'Laís',     'Rua ggg'),
(8,  'Eduarda',  'Rua hhh'),
(9,  'Carolina', 'Rua iii'),
(10, 'Carlos',   'Rua jjj');

INSERT INTO Vendas VALUES
(1,  1,  5,  2, '2026-03-01'),
(2,  1,  9,  1, '2026-03-02'),
(3,  1,  10, 3, '2026-03-03'),
(4,  1,  1,  1, '2026-03-04'),
(5,  2,  1,  2, '2026-03-05'),
(6,  2,  2,  4, '2026-03-06'),
(7,  3,  7,  1, '2026-03-07'),
(8,  4,  8,  5, '2026-03-08'),
(9,  4,  9,  2, '2026-03-09'),
(10, 4,  10, 1, '2026-03-10'),
(11, 5,  6,  3, '2026-03-11'),
(12, 6,  6,  2, '2026-03-12'),
(13, 7,  10, 1, '2026-03-13'),
(14, 8,  3,  4, '2026-03-14'),
(15, 8,  6,  2, '2026-03-15'),
(16, 8,  10, 1, '2026-03-16'),
(17, 9,  9,  3, '2026-03-17'),
(18, 9,  10, 2, '2026-03-18'),
(19, 10, 3,  1, '2026-03-19'),
(20, 10, 4,  5, '2026-03-20');
