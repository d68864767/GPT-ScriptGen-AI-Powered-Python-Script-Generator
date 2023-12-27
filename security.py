```python
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def secure_data(data):
    """
    Encrypts an API key
    """
    key = load_key()
    encoded_data = data.encode()
    f = Fernet(key)
    encrypted_data = f.encrypt(encoded_data)
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Decrypts an encrypted API key
    """
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

def get_env_var(var_name):
    """
    Get the environment variable or return exception
    """
    try:
        return os.getenv(var_name)
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise Exception(error_msg)

if __name__ == "__main__":
    api_key = get_env_var("API_KEY")
    encrypted_api_key = secure_data(api_key)
    decrypted_api_key = decrypt_data(encrypted_api_key)
    print(f"Encrypted API Key: {encrypted_api_key}")
    print(f"Decrypted API Key: {decrypted_api_key}")
```
