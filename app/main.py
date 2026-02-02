from quart import Quart

def create_app(*args, **kwargs):
    app = Quart(__name__)

    from app.routes.index import index_bp
    app.register_blueprint(index_bp)

    return app

app = create_app()
