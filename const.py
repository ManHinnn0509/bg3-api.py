import os

from dotenv import load_dotenv
load_dotenv()

API_SECRET = os.getenv('API_SECRET', 'my-bg3-api')

HOST_ADDRESS = os.getenv('HOST_ADDRESS', '127.0.0.1')
HOST_PORT = int(os.getenv('HOST_PORT', 1053))

# Good solution from: https://stackoverflow.com/a/65407083
ENABLE_AUTH = os.getenv('ENABLE_AUTH', 'False').lower() in ('true', '1', 't')
CASE_SENSITIVE = os.getenv('CASE_SENSITIVE', 'False').lower() in ('true', '1', 't')