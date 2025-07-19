from random import randint
from typing import Any, List

import discord
from discord import Intents, Message, Member


class RolebotClient(discord.Client):
    ethan_emoji = "<:Ethan_Lockscreen:1296924145812115486>"
    attention: List[str] = ["ATTENTION!", "LISTEN UP!", "EXTRI EXTRI READ ALL ABOUT IT!"]
    flair: List[str] = [", get a load of this guy", ", wonder what they did to deserve that",
                        " " + ethan_emoji * 3]

    _announcement_channel = None
    _announcement_channel_id: int = 1396170402274742392

    def __init__(self, *, intents: Intents, **options: Any):
        super().__init__(intents=intents, **options)

    def get_message_pieces(self):
        attention = self.attention[randint(0, len(self.attention) - 1)]
        flair = self.flair[randint(0, len(self.flair) - 1)]
        return attention, flair

    def get_announcement_channel(self):
        if self._announcement_channel is None:
            self._announcement_channel = self.get_channel(self._announcement_channel_id)
        return self._announcement_channel

    async def on_member_update(self, before: Member, after: Member):
        chan = self.get_announcement_channel()
        if before.roles < after.roles:
            new_role = next(iter([r for r in after.roles if r not in before.roles]))
            attention, flair = self.get_message_pieces()

            await chan.send(
                content=f"@here {attention} {after.name} has a new role of "
                        f"\"{new_role.name.upper()}\"{flair}")

    async def on_message_edit(self, before: Message, after: Message):
        chan = self.get_announcement_channel()
        if before.content != after.content:
            await chan.send(
                content=f"GASLIGHT WARNING: {before.author.display_name} edited their message from: \n"
                        f"\"{before.content}\"\n"
                        f"  to: \n"
                        f"\"{after.content}\"")
