# Discord Bot OBVGREEN

یک بات دیسکورد که با کامند `/OBVGREEN` تصویر مورد نظر را ارسال می‌کند.

## نصب و راه‌اندازی

### 1. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### 2. ایجاد بات در Discord Developer Portal
1. به https://discord.com/developers/applications بروید
2. "New Application" را کلیک کنید
3. نام بات را وارد کنید
4. به بخش "Bot" بروید
5. "Add Bot" را کلیک کنید
6. Token بات را کپی کنید

### 3. تنظیم Token
1. فایل `.env.example` را کپی کرده و نام آن را به `.env` تغییر دهید
2. در فایل `.env` مقدار `YOUR_ACTUAL_TOKEN_HERE` را با Token واقعی بات خود جایگزین کنید:
```
DISCORD_BOT_TOKEN=your_actual_bot_token_here
```

### 4. دعوت بات به سرور
1. در Discord Developer Portal به بخش "OAuth2" > "URL Generator" بروید
2. Scopes: `bot` و `applications.commands` را انتخاب کنید
3. Bot Permissions: `Send Messages` و `Attach Files` را انتخاب کنید
4. لینک تولید شده را کپی کرده و بات را به سرور خود دعوت کنید

### 5. اجرای بات

double click run.bat
یا روی فایل `run.bat` دابل کلیک کنید.


### 2. آپلود فایل‌ها
```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit: Discord OBVGREEN bot"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

# Push to GitHub
git push -u origin main
```

**نکته مهم:** فایل `.env` حاوی Token بات شما است و به دلایل امنیتی در `.gitignore` قرار دارد و آپلود نمی‌شود. این کار طبیعی است و Token شما محفوظ می‌ماند.

### 3. Clone کردن در کامپیوتر دیگر
اگر می‌خواهید بات را در کامپیوتر دیگری اجرا کنید:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
pip install -r requirements.txt
# سپس فایل .env را ایجاد کرده و Token را تنظیم کنید
```

## ساختار فایل‌ها
- `main.py` - کد اصلی بات
- `requirements.txt` - وابستگی‌های پایتون
- `obvgreen_image.png` - تصویر ارسالی بات
- `run.bat` - فایل اجرای سریع بات
- `.env.example` - نمونه فایل تنظیمات
- `.gitignore` - فایل‌های نادیده گرفته شده توسط Git