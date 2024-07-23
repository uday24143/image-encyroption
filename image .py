from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
import os

# Function to pad data to make it suitable for AES encryption
def pad(data):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

# Function to encrypt an image file
def encrypt_image(input_file, output_file, key):
    # Read the image file
    with open(input_file, 'rb') as f:
        image_data = f.read()

    # Pad the image data to match block size for AES
    padded_data = pad(image_data)

    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())

    # Encrypt the data
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Write the IV and encrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(iv)
        f.write(encrypted_data)

# Example usage:
if __name__ == "__main__":
    # Replace with your actual image file path
    input_file = 'image.jpg'
    output_file = 'encrypted_image.enc'

    # Generate a 256-bit key (32 bytes)
    key = os.urandom(32)

    # Encrypt the image
    encrypt_image(input_file, output_file, key)
