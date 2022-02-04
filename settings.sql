-- settings.sql
DROP DATABASE sports;
CREATE DATABASE sports;
CREATE USER sportuser WITH PASSWORD 'sports';
GRANT ALL PRIVILEGES ON DATABASE sports TO sportuser;