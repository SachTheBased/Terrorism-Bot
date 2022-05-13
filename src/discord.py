import aiohttp

class Context:
  def __init__(self, context, headers):
    self.context = context
    self.headers = headers

  async def send(self, msg):
    