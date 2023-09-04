-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 04/09/2023 às 23:35
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `colegio`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cidade`
--

CREATE TABLE `cidade` (
  `idCidade` int(11) NOT NULL,
  `nomeCidade` varchar(40) NOT NULL,
  `siglaCidade` char(3) NOT NULL,
  `idEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `cidade`
--

INSERT INTO `cidade` (`idCidade`, `nomeCidade`, `siglaCidade`, `idEstado`) VALUES
(1, 'Santa Cruz do Sul', 'SCS', 1),
(2, 'Venancio Aires', 'VA', 1),
(3, 'Cruzeiro', 'CRU', 2),
(4, 'Porto Alegre', 'POA', 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `idCliente` int(11) NOT NULL,
  `nomeCliente` varchar(60) NOT NULL,
  `dataNascimentoCliente` date NOT NULL,
  `idSexo` int(2) NOT NULL,
  `idCidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`idCliente`, `nomeCliente`, `dataNascimentoCliente`, `idSexo`, `idCidade`) VALUES
(1, 'Nairo Andre Jesus Sanches', '2013-01-15', 1, 1),
(2, 'Maria da Silva', '2017-05-06', 2, 2),
(3, 'Pedro Souza', '2001-01-04', 1, 3),
(4, 'Fernanda Noll', '2001-06-11', 2, 3),
(5, 'Pedro Silva', '1999-10-19', 1, 2),
(6, 'Pablo Souza', '1999-06-23', 1, 3),
(7, 'Camila Muller', '2000-08-23', 2, 3),
(8, 'Joana Carvalho', '1989-07-26', 2, 1),
(9, 'Pedro Teste', '0000-00-00', 1, 1),
(10, 'Pedro Novo Teste', '2000-10-31', 1, 3),
(12, 'Ana Teste', '1892-08-30', 2, 3),
(13, 'Pedro Carvalho', '2000-06-06', 1, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `estado`
--

CREATE TABLE `estado` (
  `idEstado` int(11) NOT NULL,
  `nomeEstado` varchar(30) NOT NULL,
  `siglaEstado` char(2) NOT NULL,
  `idPais` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `estado`
--

INSERT INTO `estado` (`idEstado`, `nomeEstado`, `siglaEstado`, `idPais`) VALUES
(1, 'Rio grande do Sul', 'RS', 1),
(2, 'São Paulo', 'SP', 2),
(3, 'Rio de Janeiro', 'RJ', 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `pais`
--

CREATE TABLE `pais` (
  `idPais` int(11) NOT NULL,
  `nomePais` varchar(45) NOT NULL,
  `siglaPais` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `pais`
--

INSERT INTO `pais` (`idPais`, `nomePais`, `siglaPais`) VALUES
(1, 'Brazil', 'BRA'),
(2, 'Estados Unidos ', 'EUA'),
(3, 'Canada', 'CAN');

-- --------------------------------------------------------

--
-- Estrutura para tabela `sexo`
--

CREATE TABLE `sexo` (
  `idSexo` int(2) NOT NULL,
  `nomeSexo` varchar(20) NOT NULL,
  `siglaSexo` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `sexo`
--

INSERT INTO `sexo` (`idSexo`, `nomeSexo`, `siglaSexo`) VALUES
(1, 'Masculino', 'M'),
(2, 'Feminino', 'F');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cidade`
--
ALTER TABLE `cidade`
  ADD PRIMARY KEY (`idCidade`);

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`idCliente`);

--
-- Índices de tabela `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`idEstado`);

--
-- Índices de tabela `pais`
--
ALTER TABLE `pais`
  ADD PRIMARY KEY (`idPais`);

--
-- Índices de tabela `sexo`
--
ALTER TABLE `sexo`
  ADD PRIMARY KEY (`idSexo`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cidade`
--
ALTER TABLE `cidade`
  MODIFY `idCidade` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `estado`
--
ALTER TABLE `estado`
  MODIFY `idEstado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `pais`
--
ALTER TABLE `pais`
  MODIFY `idPais` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `sexo`
--
ALTER TABLE `sexo`
  MODIFY `idSexo` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
