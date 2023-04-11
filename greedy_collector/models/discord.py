from discord_webhook import DiscordWebhook

class Discord:
  def __init__(self, webhook_url):
    self.webhook_url = webhook_url

  def send(self, message):
    webhook = DiscordWebhook(url=self.webhook_url, content=message)
    response = webhook.execute()
    print(response)
    return
