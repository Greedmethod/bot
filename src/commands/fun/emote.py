import random
import json
from highrise import User
from config.config import config


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "emote"
        self.description = "Perform a random emote on a specific player or all players in the room"
        self.permissions = ['emote']
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        prefix = config.prefix
        emotes_file = 'config/json/emotes.json'
        with open(emotes_file) as f:
            emotes = json.load(f)

        if len(args) > 0:
            response = await self.bot.highrise.get_room_users()
            users = [content[0] for content in response.content]

            if args[0] == 'all':
                for target_user in users:
                    target_user_id = target_user.id
                    emote_name = random.choice(emotes)
                    await self.bot.highrise.send_emote(emote_name, target_user_id)
                return

            target_username = args[0].lower()
            if not target_username:
                target_username = 'Hr.BotHelper'.lower()
            elif target_username.startswith('@'):
                target_username = target_username[1:]

            target_user = next(
                (user for user in users if user.username.lower() == target_username.lower()), None)
            if not target_user:
                await self.bot.highrise.send_whisper(user.id, f"User '{target_username}' not found in the room.")
                return

            target_user_id = target_user.id
        else:
            target_username = user.username.lower()
            target_user_id = user.id

        emote_name = random.choice(emotes)
        await self.bot.highrise.send_emote(emote_name, target_user_id)import random
import json
from highrise import User
from config.config import config


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "emote"
        self.aliases = ["e"]
        self.description = "Perform a random emote in the room or see the list of emotes."
        self.permissions = ["emote"]
        self.cooldown = 5

        # Load emotes from JSON
        with open("config/json/emotes.json") as f:
            self.emotes = json.load(f)

    async def execute(self, user: User, args: list, message: str):
        # Show list of emotes
        if args and args[0].lower() == "list":
            emote_list = ", ".join(self.emotes)
            await self.bot.highrise.send_whisper(user.id, f"📜 Available emotes: {emote_list}")
            return

        # Choose a random emote
        emote_name = random.choice(self.emotes)

        # Emote for everyone
        if args and args[0].lower() == "all":
            await self.bot.highrise.chat(f"🎭 {user.username} performs {emote_name} for everyone!")
            await self.bot.highrise.emote(emote_name)
            return

        # Emote at a specific user (simulate targeting via chat)
        target_username = args[0] if args else None
        if target_username:
            # Clean username
            if target_username.startswith("@"):
                target_username = target_username[1:]

            await self.bot.highrise.chat(f"🎭 {user.username} performs {emote_name} at {target_username}!")
            await self.bot.highrise.emote(emote_name)
            return

        # Default: perform emote without target
        await self.bot.highrise.chat(f"🎭 {user.username} performs {emote_name}!")
        await self.bot.highrise.emote(emote_name)
