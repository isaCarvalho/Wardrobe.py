-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 17/03/2019 às 19:01
-- Versão do servidor: 10.1.38-MariaDB
-- Versão do PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `wardrobe_py`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `roupas`
--

CREATE TABLE `roupas` (
  `id_roupa` int(11) NOT NULL,
  `categoria` varchar(255) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `tamanho` varchar(255) NOT NULL,
  `ativo` tinyint(1) NOT NULL,
  `id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `roupas`
--

INSERT INTO `roupas` (`id_roupa`, `categoria`, `descricao`, `tamanho`, `ativo`, `id_user`) VALUES
(1, 'blusa', 'blusa branca', 'm', 0, 1),
(2, 'vestido', 'vestido azul longo', 'unico', 1, 2),
(3, 'blusa', 'blusa listrada', 'p', 1, 1),
(4, 'short', 'short azul com flores', 'p', 1, 1),
(6, 'vestido', 'vestido branco', 'p', 1, 1),
(7, 'calça', 'calça preta jeans', '38', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `ativo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `users`
--

INSERT INTO `users` (`id_user`, `nome`, `email`, `senha`, `ativo`) VALUES
(1, 'Isabela', 'isabela@teste.com', 'teste', 1),
(2, 'Testando', 'testando@teste.com', 'testand', 0),
(3, 'Usuario', 'usuario@teste.com', 'user', 0);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_qt_users_categoria`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_qt_users_categoria` (
`nome` varchar(255)
,`categoria` varchar(255)
,`qt_categoria` bigint(21)
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_qt_users_roupas`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_qt_users_roupas` (
`quantidade` bigint(21)
,`nome` varchar(255)
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_qt_users_tamanho`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_qt_users_tamanho` (
`nome` varchar(255)
,`tamanho` varchar(255)
,`qt_tamanho` bigint(21)
);

-- --------------------------------------------------------

--
-- Estrutura para view `vw_qt_users_categoria`
--
DROP TABLE IF EXISTS `vw_qt_users_categoria`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_qt_users_categoria`  AS  select `users`.`nome` AS `nome`,`roupas`.`categoria` AS `categoria`,count(`roupas`.`categoria`) AS `qt_categoria` from (`users` join `roupas`) where (`roupas`.`id_user` = `users`.`id_user`) group by `roupas`.`id_user`,`roupas`.`categoria` ;

-- --------------------------------------------------------

--
-- Estrutura para view `vw_qt_users_roupas`
--
DROP TABLE IF EXISTS `vw_qt_users_roupas`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_qt_users_roupas`  AS  select count(`roupas`.`id_user`) AS `quantidade`,`users`.`nome` AS `nome` from (`roupas` join `users`) where (`users`.`id_user` = `roupas`.`id_user`) group by `roupas`.`id_user` ;

-- --------------------------------------------------------

--
-- Estrutura para view `vw_qt_users_tamanho`
--
DROP TABLE IF EXISTS `vw_qt_users_tamanho`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_qt_users_tamanho`  AS  select `users`.`nome` AS `nome`,`roupas`.`tamanho` AS `tamanho`,count(`roupas`.`tamanho`) AS `qt_tamanho` from (`users` join `roupas`) where (`roupas`.`id_user` = `users`.`id_user`) group by `roupas`.`id_user`,`roupas`.`tamanho` ;

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `roupas`
--
ALTER TABLE `roupas`
  ADD PRIMARY KEY (`id_roupa`),
  ADD KEY `id_users` (`id_user`);

--
-- Índices de tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `roupas`
--
ALTER TABLE `roupas`
  MODIFY `id_roupa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `roupas`
--
ALTER TABLE `roupas`
  ADD CONSTRAINT `roupas_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
