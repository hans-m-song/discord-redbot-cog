from .mycog import Mycog


def setup(bot):
    cog = Mycog(bot)
    bot.add_cog(cog)
