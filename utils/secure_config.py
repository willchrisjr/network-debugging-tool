from cryptography.fernet import Fernet
import json
import os

class SecureConfig:
    def __init__(self, config_file='secure_config.json', key_file='secret.key'):
        self.config_file = config_file
        self.key_file = key_file
        self.key = self._load_or_generate_key()
        self.fernet = Fernet(self.key)

    def _load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key

    def save_config(self, config):
        encrypted_config = self.fernet.encrypt(json.dumps(config).encode())
        with open(self.config_file, 'wb') as f:
            f.write(encrypted_config)

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'rb') as f:
                encrypted_config = f.read()
            decrypted_config = self.fernet.decrypt(encrypted_config)
            return json.loads(decrypted_config)
        return {}

# Usage example:
# secure_config = SecureConfig()
# secure_config.save_config({'api_key': 'your_secret_api_key'})
# config = secure_config.load_config()
# api_key = config.get('api_key')

