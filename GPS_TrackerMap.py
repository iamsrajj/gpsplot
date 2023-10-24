import mysql.connector
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

# Replace these with your MySQL database credentials
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root@1234',
    database='gps_tracker_db'
)


@app.route('/get_coordinates', methods=['GET'])
def get_coordinates():
    cursor = db.cursor()
    cursor.execute("SELECT longitude, latitude, speed FROM gps_data")
    data = cursor.fetchall()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='103.76.249.121', port=5000, debug=True)
