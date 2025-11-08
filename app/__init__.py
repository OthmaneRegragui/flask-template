import os
from flask import Flask
from .extensions import db, migrate
from .auto_loader import auto_route_handler

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.config.settings.DevelopmentConfig')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    db.init_app(app)
    migrate.init_app(app, db)

    methods = ['GET', 'POST']
    app.add_url_rule('/', 'auto_route_index', lambda: auto_route_handler(''), methods=methods)
    app.add_url_rule('/<path:path>', 'auto_route_path', auto_route_handler, methods=methods)

    return app