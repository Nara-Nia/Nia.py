from discord.ext import commands
import discord

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='comandos')
    async def commands_list(self, ctx):
        embed = discord.Embed(
            title="Comandos do Bot",
            description="Aqui estão os comandos disponíveis:",
            color=discord.Color.blue()
        )
        embed.add_field(name="!ping", value="Responde com 'Pong!'.", inline=False)
        embed.add_field(name="!ban [membro] [razão]", value="Bane um membro do servidor.", inline=False)
        embed.add_field(name="!lock", value="Priva canais de membros comuns", inline=False)
        # Adicione mais comandos aqui conforme necessário
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))


