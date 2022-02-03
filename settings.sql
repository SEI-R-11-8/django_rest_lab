-- settings.sql
CREATE DATABASE django_rest_lab;
CREATE USER django_rest_labuser WITH PASSWORD 'django_rest_lab';
GRANT ALL PRIVILEGES ON DATABASE django_rest_lab TO django_rest_labuser;