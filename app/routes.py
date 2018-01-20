from app import app
from config import config

PATH = '/' + config.BOT_TOKEN
DUMMY_PATH = '/' + 'hello'
@app.route(DUMMY_PATH)
def index():
    return 'Hello, Cruel World!\n'
