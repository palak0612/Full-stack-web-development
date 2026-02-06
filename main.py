from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
from config import config

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = app.config["SECRET_KEY"]

def get_db_connection():
  return pymysql.connect(
    host = app.config["MYSQL_HOST"],
    user= app.config["MYSQL_USER"],
    password= app.config["MYSQL_PASSWORD"],
    database= app.config["MYQL_DATABASE"],
    port= app.config["MYSQL_PORT"]
  )

app = Flask(__name__)
app.secret_key = "red"
app.secret_key = app.config["SECRET_KEY"]

users = {}  #this will take one user in a session

@app.route("/")
def home():
    return redirect(url_for("index"))

@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("select id from users where username = %s",(u,))
        existing = cur.cursor()
        
        if existing:
          cur.close()
          conn.close()
          return render_template("register.html", msg="User  exists!")
        
        
        cur.execute("insert into users(username,password) values(%s,%s)", (u,p))
        cur.commit()
        cur.close()
        conn.close()
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        if users.get(u) == p:
            session["user"] = u
            return redirect(url_for("dashboard"))

        return render_template("login.html", msg="Invalid login!")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)