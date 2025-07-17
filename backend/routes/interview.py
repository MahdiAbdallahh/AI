from flask import Blueprint, request, jsonify
from services.openai_interview import call_openrouter
from utils.prompts import build_interview_prompt

interview_bp = Blueprint("interview", __name__)

@interview_bp.route("/mock", methods=["POST"])
def handle_mock_interview():
    try:
        data = request.get_json()

        # Validation
        if not data or "message" not in data or "role" not in data:
            return jsonify({
                "success": False,
                "error": "Missing required fields: message, role"
            }), 400

        user_message = data.get("message", "")
        history = data.get("history", [])  # list of {question, answer}
        resume = data.get("resume", "")
        role = data.get("role", "Software Engineer")

        # Build messages
        messages = [{
            "role": "system",
            "content": build_interview_prompt(role, resume)
        }]

        for item in history:
            messages.append({"role": "assistant", "content": item["question"]})
            messages.append({"role": "user", "content": item["answer"]})

        if user_message:
            messages.append({"role": "user", "content": user_message})

        # Call model
        reply = call_openrouter(messages)

        return jsonify({
            "success": True,
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
