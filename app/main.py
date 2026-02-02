# app/main.py
from quart import Quart

def create_app(*args, **kwargs):
    app = Quart(__name__)

    from app.routes.index import index_bp
    app.register_blueprint(index_bp)

    from app.routes.sanitize import sanitize_bp
    app.register_blueprint(sanitize_bp)

    return app

app = create_app()
