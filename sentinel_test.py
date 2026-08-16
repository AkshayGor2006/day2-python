import os
API_KEY = os.getenv("API_KEY")

PASSWORD = "admin123"

SECRET_KEY = "my_super_secret"

API_KEY_FROM_ENV = os.getenv("API_KEY")

password_hash = hash_password("hello")

normal_value = "hello"
