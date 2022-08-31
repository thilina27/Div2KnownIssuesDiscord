import os
from datetime import datetime
import discord
import divisionData
from divisionData import get_data
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
target_channel_id = os.getenv('TARGET')
bot.data = {}
data = {}
intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True


@tasks.loop(hours=24)
async def reported_data():
    message_channel = await bot.fetch_channel(target_channel_id)
    bot.data = get_data()
    message1 = "**The Division 2 Known Issues** \n " + datetime.today().strftime('%Y-%m-%d') + "\n\n\n"

    message1 += "**" + divisionData.Reported + "** 📖 \n\n"
    for _isu in bot.data.reported:
        message1 += str(_isu)

    message2 = "\n**" + divisionData.Investigating + "** 🔍 \n\n"
    for _isu in bot.data.investigating:
        message2 += str(_isu)

    message3 = "\n**" + divisionData.In_Progress + "** 🛠\n\n"
    for _isu in bot.data.in_progress:
        message3 += str(_isu)

    message4 = "\n**" + divisionData.Fix_Ready + "** 👍 \n\n"
    for _isu in bot.data.fix_ready:
        message4 += str(_isu)

    message5 = "\n\n**" + divisionData.Fix_Live + "** ✅\n\n"
    for _isu in bot.data.fix_live:
        message5 += str(_isu)

    all_messages = [message1, message2, message3, message4, message5]
    for message in all_messages:
        await message_channel.send(message + "**---------------------**")
    print(reported_data.current_loop)


@reported_data.after_loop
async def after_slow_count():
    print('done!')

reported_data.start()
bot.run(TOKEN)
