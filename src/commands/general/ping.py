from highrise import User


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "ping"
        self.description = "Responds with pong."
        self.aliases = ["latency"]
        self.cooldown = 1

    async def execute(self, user: User, args: list, message: str):
        await self.bot.highrise.chat("pong")
