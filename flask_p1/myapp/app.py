from flask import Flask
from myapp.configs import RegexConverter,DevelopmentConfig,TestingConfig,ProductionConfig
from myapp.api import blue
from myapp.exts import db,api
def create_app():
    app=Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.url_map.converters["regex"]=RegexConverter
    db.init_app(app)
    api.init_app(app)
    app.register_blueprint(blue)
    return app