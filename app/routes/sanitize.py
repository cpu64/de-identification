# app/routes/sanitize.py
from quart import Blueprint, request, jsonify
from app.services.sanitize import sanitize

sanitize_bp = Blueprint("sanitize", __name__)

@sanitize_bp.route("/sanitize", methods=["POST"])
async def sanitize_text():
    data = await request.get_json()

    text = data.get("text", "")

    sanitized = await sanitize(text)

    return jsonify({"sanitized": sanitized})
