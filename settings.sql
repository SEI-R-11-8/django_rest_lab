-- settings.sql
CREATE DATABASE la_liga;
CREATE USER la_liga_user WITH PASSWORD 'liga';
GRANT ALL PRIVILEGES ON DATABASE la_liga TO la_liga_user;