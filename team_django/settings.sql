DROP DATABASE team;

CREATE DATABASE team;
CREATE USER teamuser WITH PASSWORD 'team';
GRANT ALL PRIVILEGES ON DATABASE team TO teamuser;
