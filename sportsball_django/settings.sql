-- settings.sql
CREATE DATABASE sportsball;
CREATE USER sportsballuser WITH PASSWORD 'sportsball';
GRANT ALL PRIVILEGES ON DATABASE sportsball TO sportsballuser;