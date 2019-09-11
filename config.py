import os

from dotenv import load_dotenv
load_dotenv()

class Config:

   	news_sources_url ='https://newsapi.org/v2/sources?&apiKey={}'
   	articles_url = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
   	API_KEY = os.environ.get('API_KEY')
   	@staticmethod
   	def init_app(app):
   		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}