from discord.ext import commands
import discord

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban_member(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            embed = discord.Embed(
                title="Erro",
                description="Você não pode se banir!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Banimento",
                description=f'{member.name} foi banido do servidor.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(
                title="Erro",
                description="Não tenho permissão para banir esse membro.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ModerationCommands(bot))
