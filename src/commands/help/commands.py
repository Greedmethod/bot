from highrise import User


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "commands"
        self.aliases = ["cmds", "list"]
        self.description = "List available commands"
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        unique_commands = {
            id(command): command for command in self.bot.command_handler.commands.values()
        }.values()

        lines = []
        for command in unique_commands:
            command_name = getattr(command, "name", None)
            if not command_name:
                continue

            description = getattr(command, "description", None)
            if description:
                lines.append(f"/{command_name} - {description}")
            else:
                lines.append(f"/{command_name}")

        lines.sort(key=str.casefold)

        if not lines:
            await self.bot.highrise.send_whisper(user.id, "No commands are currently loaded.")
            return

        await self.bot.highrise.send_whisper(user.id, "Available commands:\n" + "\n".join(lines))
