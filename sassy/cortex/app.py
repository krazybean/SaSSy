import os
from flask import Flask
from flasgger import Swagger
from sassy.cortex import config

app = Flask(__name__)
Swagger(app)

# If no environment variable set then default to development
app.config.update(**config.DevelopmentConfig.__dict__)


# Circular reference as explained in Flask 1.0 docs

from sassy.cortex.views import base
app.register_blueprint(base.api, url_prefix='/api')


if __name__ == '__main__':
    app.run()

