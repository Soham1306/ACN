from cryptography.fernet import Fernet

# Generate the key
key = Fernet.generate_key()

# Print the key so you can copy it
print("🔑 Generated Fernet key:")
print(key.decode())
