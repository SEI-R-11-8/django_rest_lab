-- settings.sql
CREATE DATABASE rest_app;
CREATE USER rest_app_user WITH PASSWORD 'rest_app';
GRANT ALL PRIVILEGES ON DATABASE rest_app TO rest_app_user;