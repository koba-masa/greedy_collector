import os
from models.discord import Discord

class Security(Discord):
  def __init__(self):
    super().__init__(os.environ['DISCORD_WEBHOOK_URL_SECURITY'])
