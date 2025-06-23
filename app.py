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

@app.route("/view")
def view():
   conn = sqlite3.connect(DATABASE)
   cur = conn.cursor()
   cur.execute("SELECT * FROM navy677")
   all_rec = cur.fetchall()  #all_rec = [(1,"naveen",21), (2,"akash", 22)]
   conn.close()
   return render_template("view.html", records=all_rec) #records = [(1,"naveen",21), (2,"akash", 22)]

@app.route("/delete/<int:id>", methods = ["POST", "GET"])
def delete(id):
   conn = sqlite3.connect(DATABASE)
   cur = conn.cursor()
   cur.execute("DELETE FROM navy677 WHERE id = ?", (id,))
   conn.commit()
   conn.close()
   return redirect("/view")

@app.route("/update/<int:id>", methods = ["POST", "GET"])
def update(id):
   if request.method == "POST":
      conn = sqlite3.connect(DATABASE)
      cur = conn.cursor()
      name = request.form["name"]
      age = request.form["age"]
      cur.execute("UPDATE navy677 SET name = ?, age = ? WHERE id = ?", (name, age, id))
      conn.commit()
      conn.close()
      return redirect("/view")
   else:
      conn = sqlite3.connect(DATABASE)
      cur = conn.cursor()
      cur.execute("SELECT * FROM navy677 WHERE id = ?",(id,))
      record = cur.fetchone() #record = [16,"rahul", 30]
      conn.close()
      return render_template("update.html", i = record) #i = [16, "rahul", 30]


# Only for local development
if __name__ == "__main__":
   app.run(debug=True)

