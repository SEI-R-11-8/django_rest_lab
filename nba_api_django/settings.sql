-- settings.sql
CREATE DATABASE nba_api;
CREATE USER nba_api_admin WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE nba_api TO nba_api_admin;