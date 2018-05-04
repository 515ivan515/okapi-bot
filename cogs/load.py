from discord.ext import commands
all_cogs = ['cogs.perms', 'cogs.load', 'cogs.simple']
prefix_cogs = 'cogs.'
class LoadCog:

    def __init__(self, bot):
        self.bot = bot
        self.all_cogs = all_cogs
        self.prefix_cogs = prefix_cogs

#--------------------
#  ..load
#--------------------
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        if cog.startswith('cogs.'):
            if cog == 'cogs.all':
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
        else:
            cog = self.prefix_cogs + cog
            if cog == 'cogs.all':
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

#--------------------
#  ..unload
#--------------------
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):

        if cog.startswith('cogs.'):
            if cog == 'cogs.all':
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
        else:
            cog = self.prefix_cogs + cog
            if cog == 'cogs.all':
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

#--------------------
#  ..reload
#--------------------
    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):

        if cog.startswith('cogs.'):
            if cog == 'cogs.all':
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
        else:
            cog = self.prefix_cogs + cog
            if cog == 'cogs.all':
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
