#imports
from disnake.ext import commands
import disnake


#create class
class main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #cog listener to print in terminal status
  @commands.Cog.listener()
  async def on_ready(self):
    print('main cog - ACTIVATED')

def setup(bot):
  bot.add_cog(main(bot))
