from flask import Flask

def create_app(config='covid19estimator.settings'):
    app = Flask(__name__)
    app.config.from_object(config)
    from .api import api_bp
    app.register_blueprint(api_bp)

    return app