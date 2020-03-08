import discord
from redbot.core import commands, checks
from redbot.core.config import Config
from utils import save, load

class Mycog(commands.Cog):
    """
    custom channel commands
    """

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=123456789,
            force_registration=True,
        )

    """ emotes """

    @commands.command()
    async def dance(self):
        await self.bot.say("<:FunkyFresh1:420881657155944449> <:FunkyFresh2:420886749150183424> <:FunkyFresh3:420888356545888257>")
    
    @commands.command(pass_context=True)
    async def report(self, ctx, user: discord.User=None):
        """ Reports a user for bad behaviour """
        s = " <:ZeldJape:419477378612330532> invalid user"
        if user.id != '343732777075736586':
            s = "<:wewlad:421930382263451648> what a bad boi " + user.mention + " <:wewlad:421930382263451648>"
        await self.bot.say(s)

    @commands.command(pass_context=True)
    async def noU(self, ctx, user : discord.User=None):
        nou = '<:NoU:420892377885048833> :regional_indicator_n::regional_indicator_o:  :regional_indicator_u:  '
        s = nou + ctx.message.author.mention
        if user:
            s = nou + user.mention
        await self.bot.say(s)

    """ misc """

    @commands.command(pass_context=True)
    async def lewd(self, ctx, user : discord.User=None):
        s = "**notices " + ctx.message.author.mention + "'s bulge** OwO what's this?"
        if user:
            s = "**notices " + user.mention + "'s bulge** OwO what's this?"
        await self.bot.say(s)

    @commands.command()
    async def penis(self, user : discord.Member):
        """Detects user's penis length
        This is 100% accurate."""
        random.seed(user.id)
        p = "8" + "="*random.randint(0, 30) + "D"
        await self.bot.say("Size: " + p)

    @commands.command()
    async def lenny(self):
        """Displays a random ASCII face."""
        ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '¯/\_{}_/¯', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '/\({})/', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
        eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
        mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
        lenny = choice(ears).format(choice(eyes)).format(choice(mouth))
        await self.bot.say(lenny)
