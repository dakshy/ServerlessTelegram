# ServerlessTelegram

A Python Serverless Telegram bot which can be hosted on <https://vercel.com>. This repo provides just an example. When deployed correctly, the bot replies with a message "Hello" to every message sent to it.

## Steps

### 1) Add env variable to vercel.com

Add your telegram bot token as `BOT_TOKEN` variable on Vercel.

### 2) Register webhook

``` bash
curl "https://api.telegram.org/bot<BOT_TOKEN>/setWebhook?url=https://{your-project-name}.vercel.app/api"
```
Cannot run the above command? Just ping the URL once on your browser and the work is done.

## Libraries

- python-telegram-bot
- flask

## Credits

- <a href="https://github.com/dakshy">dakshy</a>
