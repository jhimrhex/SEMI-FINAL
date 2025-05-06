import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "Fullname: Jhim Rhex Mejos Lumanao<br>"
        "Section: BSIT III-A 2nd LAB<br>"
        "Subject: System Integration and Architecture 1<br>"
        "Exam: Semi-Final"
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)