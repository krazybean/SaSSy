from sassy.cortex.app import app

app.logger.debug("Why aint this working?")


@app.route('/')
def index():
    app.logger.debug("TESTINGFOO!")
    return 'Hello World!'
