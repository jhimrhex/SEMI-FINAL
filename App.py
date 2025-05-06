import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "Fullname: Jhim Rhex M. Lumanao<br>"
        "Section: BSIT III-A 2nd LAB<br>"
        "Subject: System Integration and Architecture<br>"
        "Exam: Semi-Final Exam"
    )

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)