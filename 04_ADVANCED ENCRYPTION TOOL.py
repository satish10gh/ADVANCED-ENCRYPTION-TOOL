from cryptography.fernet import Fernet
import os

# ---------- GENERATE KEY ---------- #
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Key generated and saved as secret.key")


# ---------- LOAD KEY ---------- #
def load_key():
    if not os.path.exists("secret.key"):
        print("❌ Key not found! Generate key first.")
        return None

    return open("secret.key", "rb").read()


# ---------- ENCRYPT FILE ---------- #
def encrypt_file():
    key = load_key()
    if key is None:
        return

    filename = input("Enter file name to encrypt: ").strip()

    if not os.path.exists(filename):
        print("❌ File not found!")
        return

    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print("✅ File encrypted successfully!")


# ---------- DECRYPT FILE ---------- #
def decrypt_file():
    key = load_key()
    if key is None:
        return

    filename = input("Enter encrypted file name: ").strip()

    if not os.path.exists(filename):
        print("❌ File not found!")
        return

    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    try:
        decrypted_data = f.decrypt(data)
    except:
        print("❌ Decryption failed! Wrong key or corrupted file.")
        return

    output_file = "decrypted_" + filename.replace(".enc", "")

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print(f"✅ File decrypted successfully as {output_file}")


# ---------- MENU ---------- #
def main():
    while True:
        print("\n===== AES ENCRYPTION TOOL =====")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            encrypt_file()
        elif choice == "3":
            decrypt_file()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()