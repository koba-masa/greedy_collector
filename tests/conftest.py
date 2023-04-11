import sys
import os
from dotenv import load_dotenv

base_path = os.path.dirname(os.path.abspath(__file__)) + "/../"

sys.path.append(os.path.abspath(base_path))

load_dotenv('.env')
