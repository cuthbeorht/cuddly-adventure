from app import app

@app.route("/user")
def user():
    return "I'm here."
