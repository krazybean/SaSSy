from sassy.cortex.app import app
from sassy.utils import logger

log = logger.logger


@app.route('/')
def index():
    return 'Hello World!'
