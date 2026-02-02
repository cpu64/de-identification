from quart import Blueprint, render_template

index_bp = Blueprint("index", __name__)

@index_bp.route("/")
async def index():
    return await render_template("index.html")
