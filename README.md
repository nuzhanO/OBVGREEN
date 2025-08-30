# Discord OBVGREEN Bot 🤖

Hey there! I'm **TuryTury** and I created this awesome Discord bot that sends a cool OBVGREEN image whenever someone uses the `/OBVGREEN` slash command. Pretty neat, right?

## What does this bot do? 🎯

Simple! When you type `/OBVGREEN` in Discord, my bot will instantly send the OBVGREEN image. It's that easy!

## Getting Started 🚀

### Step 1: Install the required packages
First, you'll need to install the dependencies:
```bash
pip install -r requirements.txt
```

### Step 2: Create your Discord bot
1. Head over to https://discord.com/developers/applications
2. Click "New Application" and give it a cool name
3. Go to the "Bot" section and click "Add Bot"
4. Copy your bot token (you'll need this!)

### Step 3: Set up your bot token
I've made this super secure! Here's what you need to do:
1. Copy the `.env.example` file and rename it to `.env`
2. Open the `.env` file and replace `YOUR_ACTUAL_TOKEN_HERE` with your real bot token:
```
DISCORD_BOT_TOKEN=your_actual_bot_token_here
```

### Step 4: Invite the bot to your server
1. In the Discord Developer Portal, go to "OAuth2" > "URL Generator"
2. Select `bot` and `applications.commands` scopes
3. For permissions, select `Send Messages` and `Attach Files`
4. Copy the generated URL and invite your bot!

### Step 5: Run the bot
You have two options:
- Run `python main.py` in your terminal
- Or just double-click the `run.bat` file (I made this for convenience!)

## How to use it 💬

Once your bot is online, just type `/OBVGREEN` in any channel where the bot has permissions, and boom! 💥 The image will be sent instantly.

## Want to change the image? 🖼️

No problem! Just replace the `obvgreen_image.png` file with whatever image you want. The bot will automatically use your new image.

## Need help? 🤝

If you run into any issues, double-check that:
1. Your bot token is correctly set in the `.env` file
2. Your bot has the right permissions in your Discord server
3. All dependencies are installed

That's it! Enjoy your new Discord bot! 🎉

---

*Made with ❤️ by TuryTury*

