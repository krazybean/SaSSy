from sassy.cortex.app import app


@app.route('/')
def index():
    app.logger.debug("TESTINGFOO!")
    return 'Hello World!'
