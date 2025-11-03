from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
print("Encryption Key:", key.decode())

# Create cipher object
cipher = Fernet(key)

# Original message
message = "Hello, World!".encode()

# Encryption
encrypted = cipher.encrypt(message)
print("Encrypted String:", encrypted.decode())

# Decryption
decrypted = cipher.decrypt(encrypted)
print("Decrypted String:", decrypted.decode())

