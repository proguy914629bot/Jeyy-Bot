from discord.ext import commands
from io import BytesIO
import discord
import importlib
import typing
from collections import OrderedDict

from utils import imaging, useful, converters
importlib.reload(useful)
importlib.reload(imaging)
importlib.reload(converters)

from utils.imaging import *
from utils.converters import ToImage


class IMAGE(commands.Cog, name="Image"):
	"""Image generation/manipulation commands"""
	
	def __init__(self, bot):
		self.bot = bot
		self.bot.image_cache = {}
		self.thumbnail = "https://cdn.jeyy.xyz/image/patpat_4fe81e.gif"

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"Image Cog Loaded")

	async def cache_check(self, ctx, func, buf, *args):
		cmd = ctx.command.qualified_name
		img_data = str(list(Image.open(buf).getdata()))

		self.bot.image_cache.setdefault(cmd, OrderedDict())

		result = self.bot.image_cache[cmd].get(img_data)
		if result:
			result.seek(0)
			return result

		buf = await func(buf, *args)
		self.bot.image_cache[cmd][img_data] = buf
		if len(self.bot.image_cache[cmd]) > 10:
			self.bot.image_cache[cmd].popitem(last=True)

		return buf

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def cinema(self, ctx, imgb: ToImage = None):
		"""Box Office"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, cinema_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "cinema.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def pyramid(self, ctx, imgb: ToImage = None):
		"""Aliens made this"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, pyramid_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "pyramid.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def ripped(self, ctx, imgb: ToImage = None):
		"""Ripped paper"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, ripped_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "ripped.png"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def stretch(self, ctx, imgb: ToImage = None):
		"""Elastic"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, stretch_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "stretch.gif"))

	@commands.command(usage="<User|Member|Emoji|URL> <horizontal|vertical|circle>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def tunnel(self, ctx, imgb: ToImage = None, direction=None):
		"""To where?"""
		async with ctx.typing():
			if direction and direction.lower() not in ['h', 'horizontal', 'v', 'vertical', 'c', 'circle', 'r', 'rotate']:
				ctx.command.reset_cooldown(ctx)
				return await ctx.reply('Direction must be either `h`, `horizontal`, `v`, `vertical`, `c`, `circle`, `r`, or `rotate`')

			buf = await tunnel_func(imgb or await ToImage.none(ctx), direction)

			await ctx.reply(file=discord.File(buf, "tunnel.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def zonk(self, ctx, imgb: ToImage = None):
		"""zONk"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, zonk_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "zonk.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=['dot'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def dots(self, ctx, imgb: ToImage = None):
		"""Bunch of dots"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, dots_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "dots.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def knit(self, ctx, imgb: ToImage = None):
		"""Grandma made"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, knit_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "knit.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def plank(self, ctx, imgb: ToImage = None):
		"""Wooden plank"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, plank_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "plank.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def pizza(self, ctx, imgb: ToImage = None):
		"""You looks delicious"""
		async with ctx.typing():
			buf = await pizza_func(imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "pizza.png"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def shred(self, ctx, imgb: ToImage = None):
		"""Into pieces"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, shred_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "shred.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def liquefy(self, ctx, imgb: ToImage = None):
		"""Liquefying!"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, liquefy_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "liquefy.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def poly(self, ctx, imgb: ToImage = None):
		"""Triangle polygons"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, poly_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "poly.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=["plate"])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def plates(self, ctx, imgb: ToImage = None):
		"""Shaped plates"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, plates_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "plates.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def laundry(self, ctx, imgb: ToImage = None):
		"""It's getting dizzy in here"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, laundry_func, imgb or await ToImage.none(ctx))
			
			await ctx.reply(file=discord.File(buf, "laundry.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=["drug", "drugs"])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def lsd(self, ctx, imgb: ToImage = None):
		"""I'm hallucinating"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, lsd_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "lsd.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=["line"])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def lines(self, ctx, imgb: ToImage = None):
		"""Shaped lines"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, lines_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "lines.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def stereo(self, ctx, imgb: ToImage = None):
		"""Color split"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, stereo_func, imgb or await ToImage.none(ctx))
			
			await ctx.reply(file=discord.File(buf, "stereo.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=["reflect"])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def reflection(self, ctx, imgb: ToImage = None):
		"""Reflection on water"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, reflection_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "reflection.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def ipcam(self, ctx, imgb: ToImage = None):
		"""Iphone camera"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, ipcam_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "ipcam.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=["toilet"])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def flush(self, ctx, imgb: ToImage = None):
		"""Poop simulator"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, flush_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "flush.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def kanye(self, ctx, imgb: ToImage = None):
		"""Kanye holding me"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, kanye_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "kanye.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def phone(self, ctx, imgb: ToImage = None):
		"""Phone girl"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, phone_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "phone.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def neon(self, ctx, imgb: ToImage = None):
		"""Rainbow neon"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, neon_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "neon.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def shine(self, ctx, imgb: ToImage = None):
		"""You're shining"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, shine_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "shine.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=['brush'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def paint(self, ctx, imgb: ToImage = None):
		"""Gentle stroke"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, paint_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "paint.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=['box'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def cube(self, ctx, imgb: ToImage = None):
		"""A box"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, cube_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "cube.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=['wiggles', 'jiggle'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def wiggle(self, ctx, imgb: ToImage = None):
		"""Wiggle wiggle~"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, wiggle_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "wiggle.gif"))

	@commands.command(usage="<User|Member|Emoji|URL> [n_edges<3|4|5|6|7|8>=4]", aliases=['tiles'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def tile(self, ctx, imgb: ToImage = None, n_edges: typing.Literal[3, 4, 5, 6, 7, 8] = 4):
		"""Rotating tiles"""
		async with ctx.typing():
			buf = await tiles_func(imgb or await ToImage.none(ctx), n_edges)

			await ctx.reply(file=discord.File(buf, "tiles.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=['brick', 'bricks'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def wall(self, ctx, imgb: ToImage = None):
		"""A brick wall"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, bricks_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "bricks.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def letters(self, ctx, imgb: ToImage = None):
		"""Learn ABC"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, letters_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "letters.gif"))

	@commands.command(aliases=['block', 'rectangle', 'rectangles', 'rect', 'rects'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def blocks(self, ctx, imgb: ToImage = None):
		"""Blocky art"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, blocks_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "blocks.gif"))

	@commands.command(aliases=['spike'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def spikes(self, ctx, imgb: ToImage = None):
		"""Sharp edges"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, spikes_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "spikes.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def slice(self, ctx, imgb: ToImage = None):
		"""Thin slices"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, slice_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "slice.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def bayer(self, ctx, imgb: ToImage = None):
		"""Bayer filter"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, bayer_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "bayer.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def endless(self, ctx, imgb: ToImage = None):
		"""Un-ending"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, endless_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "endless.gif"))

	@commands.command(aliases=['flame'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def fire(self, ctx, imgb: ToImage = None):
		"""It's hot in here"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, fire_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "fire.gif"))

	@commands.command(aliases=['gb_cam', 'gbc'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def gameboy_camera(self, ctx, imgb: ToImage = None):
		"""Can't play kirby here"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, gameboy_camera_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "gameboy_camera.gif"))

	@commands.command(aliases=['melts'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def melt(self, ctx, imgb: ToImage = None):
		"""It's melting on my tongue!"""
		async with ctx.typing():
			buf = await melt_func(imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "melt.gif"))

	@commands.command(aliases=['crack'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def cracks(self, ctx, imgb: ToImage = None):
		"""It's cracking!"""
		async with ctx.typing():
			buf = await cracks_func(imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "cracks.png"))

	@commands.command(aliases=['planet'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def globe(self, ctx, imgb: ToImage = None):
		"""Planet Y0-oU"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, globe_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "globe.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def cow(self, ctx, imgb: ToImage = None):
		"""Holy cow!"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, cow_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "cow.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def ripple(self, ctx, imgb: ToImage = None):
		"""Water ripple"""
		async with ctx.typing():
			buf = await ripple_func(imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "ripple.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def fan(self, ctx, imgb: ToImage = None):
		"""I'm a fan"""
		async with ctx.typing():
			circled = await circle_func(imgb or await ToImage.none(ctx), (100, 100))
			buf = await self.cache_check(ctx, fan_func, circled)

			await ctx.reply(file=discord.File(buf, "fan.gif"))

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def undilate(self, ctx, imgb: ToImage = None):
		"""Remove water"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, undilate_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "undilate.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def dilate(self, ctx, imgb: ToImage = None):
		"""Add water"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, dilate_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "dilate.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def logoff(self, ctx, user: typing.Union[discord.Member, discord.User]=None):
		"""When you logoff"""
		async with ctx.typing():
			user = user or ctx.author

			img = await ctx.to_image(user)

			buf = await logoff_func(img)
			await ctx.reply(f'> {user} logging off discord <a:discordwhite:846643324790243339>', file=discord.File(buf, 'logoff.gif'), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def cloth(self, ctx, imgb: ToImage = None):
		"""It's still wet"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, cloth_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "cloth.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def bubble(self, ctx, imgb: ToImage = None):
		"""Blub blub"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, bubble_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "bubble.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def pattern(self, ctx, imgb: ToImage = None):
		"""Stitch pattern"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, pattern_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "pattern.gif"), mention_author=False)

	@commands.command(aliases=["ad", "advertize"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def ads(self, ctx, imgb: ToImage = None):
		"""CLICK FOR MORE!!!"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, advertize_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "ads.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL> [frequency=0.05] [amplitude<1|2|3|4|5>=3]")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def wave(self, ctx, imgb: ToImage = None, frequency: float=0.05, amplitude: typing.Literal[1, 2, 3, 4, 5]=3):
		"""Me wavey wavey"""
		async with ctx.typing():
			buf = await wave_func(imgb or await ToImage.none(ctx), frequency, amplitude*10)

			await ctx.reply(file=discord.File(buf, "wave.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def warp(self, ctx, imgb: ToImage = None):
		"""wwaaaaarrrpppp"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, warp_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "warp.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def sensitive(self, ctx, imgb: ToImage = None):
		"""! TW !"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, sensitive_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "sensitive.gif"), mention_author=False)

	@commands.command(aliases=["yt"], usage="<Member|User> <title>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def youtube(self, ctx, author: typing.Union[discord.Member, discord.User], *, title):
		"""Storytime when-"""
		async with ctx.typing():
			pfp = BytesIO(await author.display_avatar.read())

			buf = await youtube_func(pfp, author.name, title)

			await ctx.reply(file=discord.File(buf, "youtube.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def matrix(self, ctx, imgb: ToImage = None):
		"""9874730847802234"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, matrix_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "matrix.gif"), mention_author=False)

	@commands.command(aliases=["pprz", "ppz"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def paparazzi(self, ctx, imgb: ToImage = None):
		"""Going to Met Gala"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, paparazzi_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "paparazzi.gif"), mention_author=False)

	@commands.command(name='print', usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def _print(self, ctx, imgb: ToImage = None):
		"""Out of ink"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, print_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "print.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL> <X|Y=X>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def shear(self, ctx, imgb: ToImage = None, axis: typing.Literal['Y', 'y', 'X', 'x']='x'):
		"""Shearing tears"""
		async with ctx.typing():
			buf = await shear_func(imgb or await ToImage.none(ctx), axis)

			await ctx.reply(file=discord.File(buf, "shear.gif"), mention_author=False)

	@commands.command(aliases=['magnifying'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def magnify(self, ctx, imgb: ToImage = None):
		"""Detective business"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, magnify_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "magnify.gif"), mention_author=False)

	@commands.command(aliases=['love', 'loves', 'heart'], usage="<User|Member|Emoji|URL> <rainbow=false>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def hearts(self, ctx, imgb: ToImage = None, rainbow:bool=False):
		"""Love is in the air"""
		async with ctx.typing():
			buf = await love_func(imgb or await ToImage.none(ctx), rainbow)
			await ctx.reply(file=discord.File(buf, "hearts.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def cartoon(self, ctx, imgb: ToImage = None):
		"""Cartoonify"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, cartoon_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "cartoon.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def canny(self, ctx, imgb: ToImage = None):
		"""Canny Edges"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, canny_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "canny.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL> <level=2>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def boil(self, ctx, imgb: ToImage = None, level:int=2):
		"""It's HOT!"""
		async with ctx.typing():
			if level < 1 or level > 5:
				return await ctx.reply("Boiling level should be an integer between 1 and 5, inclusive.", mention_author=False)
			buf = await boil_func(imgb or await ToImage.none(ctx), level)

			await ctx.reply(file=discord.File(buf, "boil.gif"), mention_author=False)

	@commands.command(aliases=['abs'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def abstract(self, ctx, imgb: ToImage = None):
		"""Piccasso"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, abstract_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "abstract.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def shock(self, ctx, imgb: ToImage = None):
		"""WHAT!"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, shock_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "shock.gif"), mention_author=False)

	@commands.command(aliases=["inf", "infinite"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def infinity(self, ctx, imgb: ToImage = None):
		"""Never ending"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, infinity_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "infinity.gif"), mention_author=False)

	@commands.command(aliases=['eq'], usage="<User|Member|Emoji|URL> <level=3>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def earthquake(self, ctx, imgb: ToImage = None, power:int=3):
		"""SAVE YOURSELF"""
		async with ctx.typing():
			buf = await earthquake_func(imgb or await ToImage.none(ctx), power)

			await ctx.reply(file=discord.File(buf, "earthquake.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def tv(self, ctx, imgb: ToImage = None):
		"""Look ma!"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, tv_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "tv.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>", aliases=["roll", "rotate"])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def spin(self, ctx, imgb: ToImage = None):
		"""Wheel simulator"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, spin_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "spin.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def lamp(self, ctx, imgb: ToImage = None):
		"""It's flickering..."""
		async with ctx.typing():
			buf = await self.cache_check(ctx, lamp_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "lamp.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def rain(self, ctx, imgb: ToImage = None):
		"""Bring your umbrella"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, rain_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "rain.gif"), mention_author=False)

	@commands.command(aliases=['optic'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def optics(self, ctx, imgb: ToImage = None):
		"""Optical Distortion"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, optic_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "optics.gif"), mention_author=False)

	@commands.command(name='half-invert', aliases=['hi', 'halfinvert', 'halfert'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def halfinvert(self, ctx, imgb: ToImage = None):
		"""Why is it not full invertion?"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, halfinvert_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "half-invert.gif"), mention_author=False)

	@commands.command(aliases=["kills"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def shoot(self, ctx, imgb: ToImage = None):
		"""A touching short movie"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, shoot_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "shoot.gif"), mention_author=False)

	@commands.command(hidden=True)
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def recent(self, ctx, channel: discord.TextChannel=None):
		async with ctx.typing():
			channel = channel or ctx.channel

			authors = []
			async for message in channel.history():
				if len(authors) > 3:
					break
				if message.author in authors:
					continue
				authors.append(message.author)
			
			if len(authors) < 3:
				authors += authors*2

			authors = authors[:3]
			authors = [BytesIO(await auth.avatar.read()) for auth in authors]
			buf = await history_func(authors)
		await ctx.reply(file=discord.File(buf, "recent.gif"), mention_author=False)
	
	@commands.command(aliases=['map'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def mcmap(self, ctx, imgb: ToImage = None):
		"""Minecraft map"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, mcmap_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "mcmap.png"), mention_author=False)

	@commands.command(aliases=['scroll', 'bar'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def bars(self, ctx, imgb: ToImage = None):
		"""Moving bars"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, scroll_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "scroll.gif"), mention_author=False)

	@commands.command(aliases=["rev"], usage="<User|Member|Emoji|URL>", hidden=True)
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def reveal(self, ctx, imgb: ToImage = None):
		"""Scroll away"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, reveal_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "reveal.gif"), mention_author=False)

	@commands.command(aliases=["sub"], usage="<User|Member|Emoji|URL>", hidden=True)
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def subtract(self, ctx, _input1: typing.Union[discord.PartialEmoji, discord.Emoji, discord.Member, discord.User, str], _input2: typing.Union[discord.PartialEmoji, discord.Emoji, discord.Member, discord.User, str]):
		"""It's just a simple math"""
		async with ctx.typing():
			if _input1 == _input2:
				return await ctx.reply("Both input cannot be the same", mention_author=False)

			_input1 = await ctx.to_image(_input1)
			_input2 = await ctx.to_image(_input2)

			buf = await subtract_func(_input1, _input2)
			await ctx.reply(file=discord.File(buf, "subtract.gif"), mention_author=False)

	@commands.command(aliases=["rad"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def radiate(self, ctx, imgb: ToImage = None):
		"""Radiates good energy"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, radiate_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "radiate.gif"), mention_author=False)

	@commands.command(aliases=["gal"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def gallery(self, ctx, imgb: ToImage = None):
		"""Create a moving gallery"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, gallery_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "gallery.gif"), mention_author=False)

	@commands.command(aliases=["layer", "lay"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def layers(self, ctx, imgb: ToImage = None):
		"""Shows layers with mirror
		Works on other gif
		"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, layer_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "layers.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def clock(self, ctx, imgb: ToImage = None):
		"""Tick-tock"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, clock_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "pie.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def heat(self, ctx, imgb: ToImage = None):
		"""Feels like on the dessert"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, pixel_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "heat.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def fry(self, ctx, imgb: ToImage = None):
		"""Till golden brown"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, fry_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "fry.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def blur(self, ctx, imgb: ToImage = None):
		"""I need glasses"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, blur_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "outoffocus.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def explicit(self, ctx, imgb: ToImage = None):
		"""Parental Advisory required"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, explicit_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "explicit_content.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def shift(self, ctx, imgb: ToImage = None):
		"""I'm not tripping, you are"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, shift_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "shift.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def zoom(self, ctx, imgb: ToImage = None):
		"""Zoom in"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, zoom_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "zoom.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def disco(self, ctx, imgb: ToImage = None):
		"""Discordtics"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, discotic_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "disco.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, aliases=['scanner'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def scan(self, ctx, imgb: ToImage = None, *, flags=None):
		"""Scan gifs"""
		async with ctx.typing():
			if flags and "--side" in flags:
				buf = await self.cache_check(ctx, time_scan_side_func, imgb or await ToImage.none(ctx))
			else:
				buf = await self.cache_check(ctx, time_scan_func, imgb or await ToImage.none(ctx))
			if not buf:
				return await ctx.reply("Only accept gif member avatar, emojis, url, tenor formats.", mention_author=False)
			await ctx.reply(file=discord.File(buf, "scan.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, aliases=['pats', 'pet', 'petpet'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def patpat(self, ctx, imgb: ToImage = None):
		"""Pat-pat--"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, patpat_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "patpat.gif"), mention_author=False)
	
	@commands.command(cooldown_after_parsing=True, aliases=['equation', 'equ'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def equations(self, ctx, imgb: ToImage = None):
		"""You're confused"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, equation_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "equations.gif"), mention_author=False)
	
	@commands.command(aliases=['ava'], usage="<User|Member>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def avatar(self, ctx, member: typing.Union[discord.Member, discord.User]=None):
		"""Get someone's avatar"""
		if not member:
			member = ctx.author

		embed = discord.Embed(title=f"{member} avatar", description=f"`{member.id}`", color=self.bot.c)
		embed.set_image(url=member.display_avatar.url)
		await ctx.reply(embed=embed, mention_author=False)

	@commands.command(aliases=['hj', 'nh', 'nohorny', 'hornijail', 'nohorni'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def hornyjail(self, ctx, bonked:discord.Member=None, bonker:discord.Member=None):
		"""Go to horny jail!"""
		async with ctx.typing():
			if not bonked:
				dataD = await ctx.to_image()
				dataR = None
			elif bonked and not bonker:
				dataD = await ctx.to_image(bonked)
				dataR = None
			elif bonked and bonker:
				dataD = await ctx.to_image(bonked)
				dataR = await ctx.to_image(bonker)
			
			buf = await nohorni_func(dataD, dataR)
			await ctx.reply(file=discord.File(buf, "hornijail.gif"), mention_author=False)

	@commands.command(usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def bomb(self, ctx, imgb: ToImage = None):
		"""Incoming explosion!"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, bomb_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "nuclear bomb.gif"), mention_author=False)

	@commands.command(aliases=['hell', 'elmo'], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def burn(self, ctx, imgb: ToImage = None):
		"""HAHAHAHAH"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, burn_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "flaming elmo.gif"), mention_author=False)

	@commands.command(aliases=['screams', 'screaming', 'AAA'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def scream(self, ctx, member:discord.Member=None):
		"""AAAAAAAAAAA"""
		async with ctx.typing():
			if not member:
				member = ctx.author

			asset = member.display_avatar.with_size(512)
			data = BytesIO(await asset.read())
			data.seek(0)

			buf = await scream_func(data)
			await ctx.reply(file=discord.File(buf, "screaam.gif"), mention_author=False)

	@commands.command()
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def why(self, ctx, member:discord.Member=None):
		"""Just.. why.."""
		async with ctx.typing():
			if not member:
				member = ctx.author

			asset = member.display_avatar.with_size(512)
			data = BytesIO(await asset.read())
			data.seek(0)

			buf = await why_func(data)
			await ctx.reply(file=discord.File(buf, "screaam.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, aliases=['sob', 'crying'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def eugh(self, ctx, member:discord.Member=None):
		"""SOBS SOBS"""
		async with ctx.typing():
			if not member:
				member = ctx.author

			asset = member.display_avatar.with_size(512)
			data = BytesIO(await asset.read())
			data.seek(0)

			buf = await eugh_func(data)
			await ctx.reply(file=discord.File(buf, "eugh.gif"), mention_author=False)

	@commands.command(aliases=['buffer'])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def buffering(self, ctx, member:discord.Member=None):
		"""Uhh.. what?"""
		async with ctx.typing():
			if not member:
				member = ctx.author

			asset = member.display_avatar.with_size(512)
			data = BytesIO(await asset.read())
			data.seek(0)

			buf = await buffering_func(data)
			await ctx.reply(file=discord.File(buf, "uhhhh.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, name="bonk", usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def bonkyy(self, ctx, imgb: ToImage = None):
		"""Bonk someone"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, bonk_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "bonked.gif"), mention_author=False)
	
	@commands.command(cooldown_after_parsing=True, name="type", hidden=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def typee(self, ctx, *args:commands.clean_content):
		"""ye. it type.
		Type your text and it'll turn into an image or a gif if you add `gif` argument on the end. Add the author by adding `auth` agument on the end. (if you're using `gif` and `auth` please type `gif` first)\nMax character: `150`\n\nExample : `j;type Lmao hii gif`
		"""
		async with ctx.typing():
			args = list(args)
			auth = ""
			if args[-1] == "auth":
				args.pop()
				if args[-1] == "gif":
					args.pop()
					if len(args) == 1:
						try:
							arg = args[0]
							arg = await commands.MessageConverter().convert(ctx, arg)
							args = [arg.clean_content]
							auth = "- " + arg.author.display_name
						except:
							auth = "- " + ctx.author.display_name
					buf, l = await types_gif(args, auth)

					if buf != "":
						await ctx.reply(file=discord.File(buf, "types.gif"), mention_author=False)
					else:
						await ctx.reply(f"Your text reached the limit of `150` characters: `{l}`", mention_author=False)
						ctx.command.reset_cooldown(ctx)

				else:
					if len(args) == 1:
						try:
							arg = args[0]
							arg = await commands.MessageConverter().convert(ctx, arg)
							args = [arg.clean_content]
							auth = "- " + arg.author.display_name
						except:
							auth = "- " + ctx.author.display_name

					buf, l = await types(args, auth)

					if buf != "":
						await ctx.reply(file=discord.File(buf, "types.png"), mention_author=False)
					else:
						await ctx.reply(f"Your text reached the limit of `150` characters: `{l}`", mention_author=False)
						ctx.command.reset_cooldown(ctx)
			
			else:
				if args[-1] == "gif":
					args.pop()
					if len(args) == 1:
						try:
							arg = args[0]
							arg = await commands.MessageConverter().convert(ctx, arg)
							args = [arg.clean_content]
						except:
							pass

					buf, l = await types_gif(args, "")

					if buf != "":
						await ctx.reply(file=discord.File(buf, "types.gif"), mention_author=False)
					else:
						await ctx.reply(f"Your text reached the limit of `150` characters: `{l}`", mention_author=False)
						ctx.command.reset_cooldown(ctx)

				else:
					if len(args) == 1:
						try:
							arg = args[0]
							arg = await commands.MessageConverter().convert(ctx, arg)
							args = [arg.clean_content]
						except:
							pass

					buf, l = await types(args, "")

					if buf != "":
						await ctx.reply(file=discord.File(buf, "types.png"), mention_author=False)
					else:
						await ctx.reply(f"Your text reached the limit of `150` characters: `{l}`", mention_author=False)
						ctx.command.reset_cooldown(ctx)

	@commands.command(cooldown_after_parsing=True, aliases=["ball"], usage="<User|Member|Emoji|URL>")
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def balls(self, ctx, imgb: ToImage = None):
		"""Ballz"""
		async with ctx.typing():
			buf = await self.cache_check(ctx, ball_func, imgb or await ToImage.none(ctx))

			await ctx.reply(file=discord.File(buf, "balls.gif"), mention_author=False)

	@commands.command(cooldown_after_parsing=True, usage="<User|Member|Emoji|URL> <level=3>")
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def glitch(self, ctx, imgb: ToImage = None, level:int=3):
		"""Glitchify"""
		if level < 1 or level > 10:
			return ctx.reply("Glitch level must be between 1 and 10.", mention_author=False)

		async with ctx.typing():
			buf = await glitch_func(imgb or await ToImage.none(ctx), level)
			await ctx.reply(file=discord.File(buf, "glitch.gif"), mention_author=False)

def setup(bot):
	bot.add_cog(IMAGE(bot))