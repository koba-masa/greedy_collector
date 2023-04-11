import os
from dotenv import load_dotenv

from models.discords.security import Security

class SecurityNotificationBot:
  def __init__(self):
    load_dotenv('.env')

  def execute(self):
    Security().send('test')

if __name__ == '__main__':
  SecurityNotificationBot().execute()
