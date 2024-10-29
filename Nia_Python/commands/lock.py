import discord
from discord.ext import commands

class LockCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lock')
    async def lock(self, ctx):
        await ctx.send("O canal foi trancado!")

# Adicionando a classe como uma extensão (certifique-se que isso está no bot principal)
async def setup(bot):
    await bot.add_cog(LockCommands(bot))
