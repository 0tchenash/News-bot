from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

CURRENT_NEWS_API_CALL = ('https://newsapi.org/v2/everything?q={query}&from={data}&sortBy=publishedAt&apiKey='+ NEWS_API_KEY
)