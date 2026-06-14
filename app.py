from flask import Flask, render_template , request , redirect
from database import (get_all_desks, get_desk, check_in, mark_away, leave_desk , return_from_away,check_expired_desks)
import threading
from time import sleep


def timer_loop():
    while True:
        try:
            check_expired_desks()
        except Exception as e:
            print(f"Timer Error: {e}")
        sleep(60)

app = Flask(__name__)
@app.route("/")
def home():
    desks = get_all_desks()
    return render_template("index.html",desks=desks)

@app.route("/desk/<int:id>", methods=["GET","POST"])
def desk(id):
    if request.method == "POST":
        occupant = request.form["occupant"]
        check_in(id,occupant)
    desk = get_desk(id)
    return render_template("desk.html",desk=desk)

@app.route("/away/<int:id>",methods=["POST"])
def away(id):
    mark_away(id)
    return redirect(f"/desk/{id}")

@app.route("/return/<int:id>",methods=["POST"])
def return_desk(id):
    return_from_away(id)
    return redirect(f"/desk/{id}")

@app.route("/leave/<int:id>",methods=["POST"])
def leave(id):
    leave_desk(id)
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    timer_thread = threading.Thread(
        target=timer_loop,
        daemon=True
    )

    timer_thread.start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )