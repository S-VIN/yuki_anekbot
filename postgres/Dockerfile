# Используем официальный образ PostgreSQL
FROM postgres:latest

# Переменные окружения для настройки базы данных
# БД за натом во локальной сети
ENV POSTGRES_DB yuki_anekbot
ENV POSTGRES_USER stepan-vinokurov
ENV POSTGRES_PASSWORD stepan-vinokurov

# Копируем скрипты миграции в контейнер
COPY init-scripts/ /docker-entrypoint-initdb.d/
