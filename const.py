import os

from dotenv import load_dotenv
load_dotenv()

API_SECRET = os.getenv('API_SECRET')

HOST_ADDRESS = os.getenv('HOST_ADDRESS')
HOST_PORT = int(os.getenv('HOST_PORT'))