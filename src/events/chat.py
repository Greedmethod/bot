from highrise.models import User
from config.config import loggers, config

async def handle_chat(self, user, message):
    print(f"DEBUG: User {user.username} has ID: {user.id}") # <--- ADD THIS LINE
    # ... rest of the code


async def on_chat(bot, user: User, message: str) -> None:
    if loggers.messages:
        print(f"{user.username}: {message}")
    if message.lstrip().startswith(config.prefix):
        await bot.command_handler.handle_command(user, message)
