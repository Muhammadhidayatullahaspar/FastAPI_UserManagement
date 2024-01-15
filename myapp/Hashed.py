import bcrypt

passwords = ["Yayat123.", "Putri123.", "Windah123.", "David123.", "Eka123."]
hashed_passwords = []

for password in passwords:
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    hashed_passwords.append(hashed.decode())

print(hashed_passwords)
