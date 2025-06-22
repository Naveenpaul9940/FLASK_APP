from flask import *
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"

# CREATE TABLE
def create():
   conn = sqlite3.connect(DATABASE)
   cur = conn.cursor()
   cur.execute('''CREATE TABLE IF NOT EXISTS navy677(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   age INTEGER NOT NULL)''')
   conn.commit()
   conn.close()

# Call create table function at import time
create()

# INSERT RECORDS TO TABLE
@app.route("/", methods=["POST", "GET"])
def index():
   if request.method == "POST":
      name = request.form["name"]
      age = request.form["age"]
      conn = sqlite3.connect(DATABASE)
      cur = conn.cursor()
      cur.execute("INSERT INTO navy677(name, age) VALUES(?, ?)", (name, age))
      conn.commit()
      conn.close()
      return redirect("/view")
   else:
      return render_template("form.html")

@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
   conn = sqlite3.connect(DATABASE)
   cur = conn.cursor()
   cur.execute("DELETE FROM navy677 WHERE id = ?", (id,))
   conn.commit()
   conn.close()
   return redirect("/view")

# FETCHING RECORDS FROM THE TABLE
@app.route("/view")
def view():
   conn = sqlite3.connect(DATABASE)
   cur = conn.cursor()
   cur.execute("SELECT * FROM navy677")
   all_rec = cur.fetchall()
   conn.close()
   return render_template("view.html", records=all_rec)

# Only for local development
if __name__ == "__main__":
   app.run(debug=True)
