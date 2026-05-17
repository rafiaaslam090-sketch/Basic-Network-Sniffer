# Secure File Transfer Application
# Python Project

import os
import shutil
from cryptography.fernet import Fernet
from datetime import datetime

# ==============================
# Generate Encryption Key
# ==============================

def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Encryption Key Generated Successfully!")

# ==============================
# Load Encryption Key
# ==============================

def load_key():
    return open("secret.key", "rb").read()

# ==============================
# Encrypt File
# ==============================

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    encrypted_file = filename + ".encrypted"

    with open(encrypted_file, "wb") as file:
        file.write(encrypted_data)

    log_activity(f"Encrypted File: {filename}")

    print("File Encrypted Successfully!")
    print("Saved as:", encrypted_file)

# ==============================
# Decrypt File
# ==============================

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    decrypted_file = "decrypted_" + filename.replace(".encrypted", "")

    with open(decrypted_file, "wb") as file:
        file.write(decrypted_data)

    log_activity(f"Decrypted File: {filename}")

    print("File Decrypted Successfully!")
    print("Saved as:", decrypted_file)

# ==============================
# Transfer File
# ==============================

def transfer_file(source, destination_folder):
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    shutil.copy(source, destination_folder)

    log_activity(f"Transferred File: {source} to {destination_folder}")

    print("File Transferred Successfully!")

# ==============================
# Audit Log
# ==============================

def log_activity(action):
    with open("audit_log.txt", "a") as log:
        log.write(f"{datetime.now()} - {action}\n")

# ==============================
# User Authentication
# ==============================

USERNAME = "admin"
PASSWORD = "1234"

def login():
    print("===== Secure File Transfer Login =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Username or Password!")
        return False

# ==============================
# Main Program
# ==============================

def main():

    if not login():
        return

    while True:

        print("\n===== MENU =====")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Transfer File")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            filename = input("Enter File Name to Encrypt: ")
            encrypt_file(filename)

        elif choice == "3":
            filename = input("Enter Encrypted File Name: ")
            decrypt_file(filename)

        elif choice == "4":
            source = input("Enter Source File Name: ")
            destination = input("Enter Destination Folder: ")
            transfer_file(source, destination)

        elif choice == "5":
            print("Program Exited.")
            break

        else:
            print("Invalid Choice!")

# ==============================
# Run Program
# ==============================

main()
