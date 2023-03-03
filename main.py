from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "are_you_my_mummy_or_daddy"
socketio = SocketIO(app)


@app.route("/", method=["POST", "GET"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
