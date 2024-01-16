CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
);

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Yayat', '$2b$12$guUx89waGiY22dLiKF2iZ.PyoDCNN9.8LHsAo0dQ/QUtEWVk1ua/C');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Putri', '$2b$12$9yFgVA7thBMdCAIT4nWVEe7.BfxYIqFwo2SHQBS2OdzjnzEVVTH/K');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Windah', '$2b$12$LQgVdfLQ3usIlSXvV23n8OimXsFrXoYcRWKiHYULPR1L08fTNIJwq');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('David', '$2b$12$yWK8ytSdv64M3Kum4jnNJOayxBjtWTIbTt39JWRjA7r8n3f1EGOj.');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Eka', '$2b$12$W1WE7eOUDDUxiprGXYm/mup5gHWoNGOBJtGq6SJJcTaBAeM6jz.eG');