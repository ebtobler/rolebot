import os
import discord
from dotenv import load_dotenv

from rolebot.rolebot_client import RolebotClient

if __name__ == "__main__":
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = RolebotClient(command_prefix="!", intents=intents)
    bot.run(token=DISCORD_TOKEN)
