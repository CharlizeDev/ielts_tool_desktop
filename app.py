from flask import Flask, request, jsonify

app = Flask(__name__)

# Fun prompts for practice mode
PROMPTS = [
    "Describe your favorite holiday memory.",
    "What do you enjoy doing in your free time?",
    "If you could learn a new skill, what would it be and why?"
]

# Motivational messages
MOTIVATIONAL_MESSAGES = [
    "Amazing effort! Keep going! 🚀",
    "You’re doing great—keep practicing! 🌟",
    "Fantastic answer! Keep shining! ✨"
]

@app.route("/")
def home():
    return "Welcome to the IELTS Speaking Practice App!"

@app.route("/ielts_test", methods=["POST"])
def ielts_test():
    data = request.get_json()
    mode = data.get("mode", "practice")
    username = data.get("username", "User")

    if mode == "practice":
        responses = []
        for question in PROMPTS:
            response = data.get(question, "No response provided.")
            feedback = {"question": question, "feedback": MOTIVATIONAL_MESSAGES[0]}
            responses.append({"response": response, "feedback": feedback})
        
        return jsonify({
            "status": "success",
            "username": username,
            "responses": responses
        })

    return jsonify({"status": "error", "message": "Invalid mode!"})

if __name__ == "__main__":
    app.run(debug=True)
