-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Мар 18 2023 г., 23:04
-- Версия сервера: 10.3.22-MariaDB
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `komitet`
--

-- --------------------------------------------------------

--
-- Структура таблицы `admin`
--

CREATE TABLE `admin` (
  `id` bigint(20) NOT NULL,
  `login` text NOT NULL,
  `prjcts` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `admin`
--

INSERT INTO `admin` (`id`, `login`, `prjcts`) VALUES
(20, '620712601', NULL),
(33, '5331959203', NULL),
(34, '830411388', NULL),
(35, '679990653', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text DEFAULT NULL,
  `e_date` datetime NOT NULL,
  `image` text DEFAULT NULL,
  `locate` text DEFAULT NULL,
  `tags` text DEFAULT NULL,
  `web_source` text DEFAULT NULL,
  `clmns` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `events`
--

INSERT INTO `events` (`id`, `name`, `description`, `e_date`, `image`, `locate`, `tags`, `web_source`, `clmns`) VALUES
(115, 'ЧтоГдеКогда', '«Что? Где? Когда?», и главное зачем? \nЗатем, чтобы проверить себя и своих друзей в области познания мира!', '2022-11-18 23:59:00', 'AgACAgIAAxkBAAIWlGNW-ciAyRSP5X9-LiDdlrIvgiHrAAKexTEbNF-4Slveoo8Y_o-yAQADAgADcwADKgQ', 'Внешнее', '0', '0', NULL),
(116, 'Чеееел', 'Опа нихуя', '2021-08-19 18:00:00', 'AgACAgIAAxkBAAIWwWNW-ysVdXGxdgG9P2z0TU9_SsvoAAKCxjEbV1W4Sh7MyOL5t-1bAQADAgADcwADKgQ', 'Внутреннее', '0', '0', NULL),
(117, 'Олеся стреляет пау пау', 'Олеся стреляет вуц пау пау, очень весело', '2022-11-12 20:00:00', 'AgACAgIAAxkBAAIXFmNW_HqK2_PQD_ixinCFA3K8JaA_AAKcvTEbKO24SjhX8frJqkEdAQADAgADcwADKgQ', 'Внутреннее', '0', 'https://www.youtube.com/', NULL),
(118, 'Вуцвуцвуц', 'Мы боги, аееее', '2023-11-12 14:00:00', 'AgACAgIAAxkBAAIXKGNW_Iqp1Q0MM-ACn33Nca8gKsuMAAKuxTEbNF-4SiJ4Jn4gav6TAQADAgADcwADKgQ', 'Внешнее', '0', '0', NULL),
(119, 'Кб-карш', 'Едем в КБ на карше', '2025-01-18 19:00:00', 'AgACAgIAAxkBAAIXS2NW_JulMyPSSTrGTHt8QuSIocYOAAKHxjEbV1W4SigK_pq1DlXCAQADAgADcwADKgQ', 'Внутреннее', '0', 'https://www.gismeteo.ru/weather-sankt-peterburg-4079/', NULL),
(122, 'Ваня дрочит письку', '24/7', '2027-06-18 15:00:00', 'AgACAgIAAxkBAAIXj2NW_QwFPn3JnvJtOxfLtUn-dmnYAAKKxjEbV1W4ShRdmLNW5FvVAQADAgADcwADKgQ', 'Внешнее', '0', '0', NULL),
(128, 'Крутое мероприятие', 'НеНочная', '2023-11-20 00:00:00', 'AgACAgIAAxkBAAJWTWPxIA4hqgABNhxqlUz0rKd25roq1wACbsYxG5wRiEuhV11fFEXeEQEAAwIAA3MAAy4E', 'Гейское', '0', '0', '_capitan_teammates1_teammates2_log'),
(129, 'Крутое мероприятие', 'НеНочная', '2023-11-20 00:00:00', 'AgACAgIAAxkBAAJW62P7oqr90kkhmq1_2YAhbz_eV3zUAAI7yDEbmJjYS-TwM6B_BG66AQADAgADcwADLgQ', 'Гейское', '0', '0', '_capitan_description_teammates1_teammates2_teammates3_log'),
(132, 'Крутое мероприятие', 'НеНочная', '2023-11-20 00:00:00', 'AgACAgIAAxkBAAJXyGQV9sbLOYlwbrDVUPa7iZ3RFKKlAALFzjEblpWwSC8gHSQ9HxOeAQADAgADcwADLwQ', 'Гейское', '0', '0', '_capitan_description_teammates1_teammates2_log'),
(133, 'Крутое мероприятие', 'НеНочная', '2023-11-20 00:00:00', 'AgACAgIAAxkBAAJX9mQWBwmC_bojSqt4ZslfG9U5k4qqAAIYzzEblpWwSJPuAY7c-7lGAQADAgADcwADLwQ', 'Гейское', '0', '0', '_capitan_teammates1_teammates2_log'),
(134, 'bvz', 'grfhdrty', '2023-09-12 20:00:00', 'AgACAgIAAxkBAAJYIGQWCI_JN21T8F45wugbeVTbz1YbAAIYzzEblpWwSJPuAY7c-7lGAQADAgADcwADLwQ', 'Внутреннее', '0', '0', '_description_log');

-- --------------------------------------------------------

--
-- Структура таблицы `inside_subs`
--

CREATE TABLE `inside_subs` (
  `id` int(11) NOT NULL,
  `login` bigint(20) NOT NULL,
  `name` text NOT NULL,
  `photo` text NOT NULL,
  `type` text DEFAULT NULL,
  `target` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `inside_subs`
--

INSERT INTO `inside_subs` (`id`, `login`, `name`, `photo`, `type`, `target`) VALUES
(63, 5331959203, 'Нагорнов Максим Николаевич', 'AgACAgIAAxkBAAJVlmPxGOpWRyppvi2S_j2VSUZBMLf8AAJoxjEbnBGISz8Cey6jSOGaAQADAgADcwADLgQ', 'razrab', '0'),
(64, 830411388, 'Савелов Дмитрий Юрьевич', 'AgACAgIAAxkBAAJWxmP7ogc0XyvO1TDcUhP3PNbqPc-dAAKOyDEbx5ThS9WzbNvlW90KAQADAgADcwADLgQ', 'razrab', '0'),
(65, 679990653, 'Никитин Максим Владимирович', 'AgACAgIAAxkBAAJXmWQV8HXHcq67oBQ2ZNaVws8nbaYeAAJWxTEbUbGxSKuHxB7T2MbrAQADAgADcwADLwQ', 'razrab', '0');

-- --------------------------------------------------------

--
-- Структура таблицы `komitet_users`
--

CREATE TABLE `komitet_users` (
  `id` bigint(20) NOT NULL,
  `name` text NOT NULL,
  `image` text DEFAULT NULL,
  `description` text NOT NULL,
  `division` text NOT NULL,
  `status` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `filling` text NOT NULL,
  `division` text NOT NULL,
  `e_date` date NOT NULL,
  `joined` text DEFAULT NULL,
  `image` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `qq_list`
--

CREATE TABLE `qq_list` (
  `for_id` int(11) NOT NULL,
  `for_log` text DEFAULT NULL,
  `for_name` text DEFAULT NULL,
  `for_description` text DEFAULT NULL,
  `for_photo` text DEFAULT NULL,
  `for_birth` text DEFAULT NULL,
  `for_faculty` text DEFAULT NULL,
  `for_group` text DEFAULT NULL,
  `for_course` text DEFAULT NULL,
  `for_phone` int(11) DEFAULT NULL,
  `for_capitan` text DEFAULT NULL,
  `for_teammates` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `qq_list`
--

INSERT INTO `qq_list` (`for_id`, `for_log`, `for_name`, `for_description`, `for_photo`, `for_birth`, `for_faculty`, `for_group`, `for_course`, `for_phone`, `for_capitan`, `for_teammates`) VALUES
(1, 'Пожалуйста, отправьте мне своё фото)', 'Ну давай же', NULL, 'Давай', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(128, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1', '2'),
(129, NULL, NULL, 'Опишите свою группу', NULL, NULL, NULL, NULL, NULL, NULL, 'Назовите главного', 'Назовите своих приспешников'),
(130, NULL, NULL, 'Опишите свою команду', NULL, NULL, NULL, NULL, NULL, NULL, 'ФИО капитана', 'ФИО спикеров'),
(132, NULL, NULL, 'fnjkdjbgf', NULL, NULL, NULL, NULL, NULL, NULL, 'vndksjvnls', 'fhjgnksjdlfg'),
(133, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '123', '321'),
(134, NULL, NULL, 'аптиапр', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `sublist07`
--

CREATE TABLE `sublist07` (
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist08`
--

CREATE TABLE `sublist08` (
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist10`
--

CREATE TABLE `sublist10` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist94`
--

CREATE TABLE `sublist94` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist95`
--

CREATE TABLE `sublist95` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist97`
--

CREATE TABLE `sublist97` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist109`
--

CREATE TABLE `sublist109` (
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist113`
--

CREATE TABLE `sublist113` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `faculty` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist115`
--

CREATE TABLE `sublist115` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist116`
--

CREATE TABLE `sublist116` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist117`
--

CREATE TABLE `sublist117` (
  `log` int(11) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist118`
--

CREATE TABLE `sublist118` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist119`
--

CREATE TABLE `sublist119` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist120`
--

CREATE TABLE `sublist120` (
  `log` int(11) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist121`
--

CREATE TABLE `sublist121` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist122`
--

CREATE TABLE `sublist122` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist128`
--

CREATE TABLE `sublist128` (
  `capitan` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates1` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates2` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `log` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist129`
--

CREATE TABLE `sublist129` (
  `capitan` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates1` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates2` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates3` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `log` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist132`
--

CREATE TABLE `sublist132` (
  `capitan` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates1` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates2` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `log` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist133`
--

CREATE TABLE `sublist133` (
  `capitan` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates1` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teammates2` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `log` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist134`
--

CREATE TABLE `sublist134` (
  `description` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `log` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `inside_subs`
--
ALTER TABLE `inside_subs`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `qq_list`
--
ALTER TABLE `qq_list`
  ADD PRIMARY KEY (`for_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `admin`
--
ALTER TABLE `admin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT для таблицы `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=135;

--
-- AUTO_INCREMENT для таблицы `inside_subs`
--
ALTER TABLE `inside_subs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT для таблицы `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
