 
from flask import Flask
from flask_cors import CORS
from routes.interview import interview_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

app.register_blueprint(interview_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
