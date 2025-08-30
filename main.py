#by TuryTury
import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')


@bot.tree.command(name='obvgreen', description='Send OBVGREEN image')
async def obvgreen(interaction: discord.Interaction):
    
    image_path = 'obvgreen_image.png'  
    
    
    if os.path.exists(image_path):
        file = discord.File(image_path)
        await interaction.response.send_message(file=file)
    else:
        await interaction.response.send_message('Image not found! Please make sure obvgreen_image.png exists in the bot directory.')


if __name__ == '__main__':
    # Get token from environment variable or use placeholder
    TOKEN = os.getenv('DISCORD_BOT_TOKEN', 'YOUR_BOT_TOKEN')
    
    if TOKEN == 'YOUR_BOT_TOKEN':
        print('Please set your Discord bot token in .env file or as environment variable DISCORD_BOT_TOKEN')
        print('Create a .env file with: DISCORD_BOT_TOKEN=your_actual_token_here')
    else:
        bot.run(TOKEN)