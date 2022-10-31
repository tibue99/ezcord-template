from dotenv import load_dotenv

from utils.bot import Bot

if __name__ == '__main__':
    load_dotenv(".env")
    bot = Bot()
    bot.run()
