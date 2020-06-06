import hashlib
import uuid

# Menggunakan metode hashing SHA256 dengan memanfaatkan built-in module hashlib dan uuid
# Informasi didapatkan dari pythoncentral.io

# Fungsi untuk merubah password user dalam bentuk hash saat signup
def hash(password):

    # Membuat susunan kata acak yang akan ditambahkan ke password user
    salt = uuid.uuid4().hex

    # Menggabungkan hasil hash password dengan salt
    hashed_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    return hashed_pass

# Fungsi untuk melakukan pengecekan apakah password yang dimasukkan saat login sesuai data user
def check(hashed_pass, user_pass):

    # Memisahkan password hasil hash di data user dari salt
    password, salt = hashed_pass.split(':')

    # Membandingkan apakah password di data user sama dengan password yang baru dimasukkan saat login
    condition = (password == (hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()))
    return condition
