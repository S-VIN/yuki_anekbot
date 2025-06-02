CREATE DATABASE yuki_anekbot;

-- Подключаемся к созданной БД
\c yuki_anekbot;

-- Создаем таблицу для анеков
CREATE TABLE aneks (
    id SERIAL PRIMARY KEY,
    anek TEXT);
