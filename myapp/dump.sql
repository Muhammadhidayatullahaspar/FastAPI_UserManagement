CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
);

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Yayat', '$2b$12$fCepX8./PcXBctafXoig3Ol0tF4nvYe4MYdznH854dXtFWm09hWp2');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Putri', '$2b$12$C4XncUIiSmC8qf3eid466.WFrUtNnOycGF5YG/tPTXwJYlpUFYnra');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Windah', '$2b$12$dQpA9RxkHn3sXl4gbOk4VO7eKdSAyJs.50mlA6GQnJp7z7CL9IdGa');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('David', '$2b$12$ysL0PmLNyypt7G0wQsgsdOvOms1q49l5WHnBbxcqMugV1yhkcicbq');

INSERT OR REPLACE INTO users (username, hashed_password) 
VALUES ('Eka', '$2b$12$NwdkvWEdG1KD5qcxvi7zruzaamW8nreVCjy5MXKLULKCzrggdTaGW');