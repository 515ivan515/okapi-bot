from discord.ext import commands
all_cogs = ['cogs.members', 'cogs.load', 'cogs.simple']
class LoadCog:

    def __init__(self, bot):
        self.bot = bot
        self.all_cogs = all_cogs

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        if cog == 'all':
            try:
                for self.all_cogs in range(len(cog)):
                    self.bot.load_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS!!!`**')
        else:
            try:
                self.bot.load_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS!!!`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        if cog == 'all':
            try:
                for cog in self.all_cogs:
                    self.bot.unload_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS!!!`**')
        else:
            try:
                self.bot.unload_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS!!!`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        if cog == 'all':
            try:
                for cog in self.all_cogs:
                    self.bot.unload_extension(cog)
                    self.bot.load_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS!!!`**')
        else:
            try:
                self.bot.unload_extension(cog)
                self.bot.load_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS!!!`**')


def setup(bot):
    bot.add_cog(LoadCog(bot))
