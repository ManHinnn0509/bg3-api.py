import os

from dotenv import load_dotenv
load_dotenv()

API_SECRET = os.getenv('API_SECRET', 'my-bg3-api')

HOST_ADDRESS = os.getenv('HOST_ADDRESS', '127.0.0.1')
HOST_PORT = int(os.getenv('HOST_PORT', 1053))