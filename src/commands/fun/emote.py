# src/commands/emote.py

import random
import json
from highrise import User
from config.config import config


class Command:
    """
    Emote command for Greedmethod/bot:
    • !emote                   → performs a random emote on self
    • !emote all               → performs a random emote on all room users
    • !emote list              → shows available emotes
    • !emote @username         → emotes the specified user
    """

    def __init__(self, bot):
        self.bot = bot
        self.name = "emote"
        self.aliases = ["e"]
        self.description = "Perform a random emote in the room"
        self.permissions = ["emote"]
        self.cooldown = 5

        # Load emotes once
        emotes_file = "config/json/emotes.json"
        try:
            with open(emotes_file, "r", encoding="utf-8") as f:
                self.emotes = json.load(f)
        except Exception as exc:
            print(f"❌ Failed to load emotes.json → {exc}")
            self.emotes = []

    async def execute(self, user: User, args: list, message: str):
        # If emotes list is empty
        if not self.emotes:
            await self.bot.highrise.send_whisper(
                user.id,
                "❌ No emotes available (config/json/emotes.json empty).",
            )
            return

        # Show available emotes
        if args and args[0].lower() == "list":
            emote_list = ", ".join(self.emotes)
            await self.bot.highrise.send_whisper(
                user.id,
                f"📜 Emotes:\n{emote_list}",
            )
            return

        # Random emote name
        emote_name = random.choice(self.emotes)

        # Emote everyone
        if args and args[0].lower() == "all":
            room_users_response = await self.bot.highrise.get_room_users()
            users = [u for u, _ in room_users_response.content]

            for u in users:
                await self.bot.highrise.send_emote(emote_name, u.id)
            return

        # Emote a specific user
        if args:
            target_username = args[0].lstrip("@").lower()

            room_users_response = await self.bot.highrise.get_room_users()
            users = [u for u, _ in room_users_response.content]

            target_user = next(
                (u for u in users if u.username.lower() == target_username),
                None,
            )
            if not target_user:
                await self.bot.highrise.send_whisper(
                    user.id,
                    f"❌ User '{target_username}' not found in the room.",
                )
                return

            await self.bot.highrise.send_emote(emote_name, target_user.id)
            return

        # Default: self emote
        await self.bot.highrise.send_emote(emote_name, user.id)