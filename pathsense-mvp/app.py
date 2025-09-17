from flask import Flask, request, jsonify, send_from_directory
import sqlite3

app = Flask(__name__)

# --- DB setup ---
def init_db():
    conn = sqlite3.connect("hazards.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS hazards
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  lat REAL, lon REAL,
                  description TEXT,
                  severity INTEGER)''')
    conn.commit()
    conn.close()

init_db()

# --- API Routes ---
@app.route("/add", methods=["POST"])
def add_hazard():
    data = request.json
    conn = sqlite3.connect("hazards.db")
    c = conn.cursor()
    c.execute("INSERT INTO hazards (lat, lon, description, severity) VALUES (?, ?, ?, ?)",
              (data["lat"], data["lon"], data["description"], data["severity"]))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

@app.route("/list", methods=["GET"])
def list_hazards():
    conn = sqlite3.connect("hazards.db")
    c = conn.cursor()
    c.execute("SELECT id, lat, lon, description, severity FROM hazards")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/")
def serve_map():
    return send_from_directory("static", "map.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
