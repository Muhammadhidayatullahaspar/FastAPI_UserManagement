-- Membuat tabel 'users'
CREATE TABLE users (
    id INTEGER PRIMARY KEY,    -- Kolom 'id' sebagai Primary Key dan auto-increment
    username TEXT UNIQUE NOT NULL, -- Kolom 'username' yang unik dan tidak boleh kosong
    hashed_password TEXT NOT NULL   -- Kolom 'hashed_password' yang tidak boleh kosong
);

-- Memasukkan data ke dalam tabel 'users'
INSERT INTO users (username, hashed_password) VALUES ('user1', 'hashedpassword1');
INSERT INTO users (username, hashed_password) VALUES ('user2', 'hashedpassword2');

-- Menambahkan data pengguna baru
INSERT INTO users (username, hashed_password) VALUES ('user3', 'hashedpassword3');
INSERT INTO users (username, hashed_password) VALUES ('user4', 'hashedpassword4');
INSERT INTO users (username, hashed_password) VALUES ('user5', 'hashedpassword5');
