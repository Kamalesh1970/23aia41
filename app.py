from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJrYW1hbGVzaGpheWFnYW5lc2hAZ21haWwuY29tIiwiZXhwIjoxNzgyODA0NDc0LCJpYXQiOjE3ODI4MDM1NzQsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiIxMjIwY2QyNC0xZThkLTQ2NzItODAyMS03ZjM0NDUzYWQ1ZTkiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJrYW1hbGVzaCBqIiwic3ViIjoiMGZiZmE3YTAtY2I2Ny00MGNlLTg1NGQtYzZiNTFhMTZlZjgyIn0sImVtYWlsIjoia2FtYWxlc2hqYXlhZ2FuZXNoQGdtYWlsLmNvbSIsIm5hbWUiOiJrYW1hbGVzaCBqIiwicm9sbE5vIjoiMjNhaWE0MSIsImFjY2Vzc0NvZGUiOiJXak55Q1QiLCJjbGllbnRJRCI6IjBmYmZhN2EwLWNiNjctNDBjZS04NTRkLWM2YjUxYTE2ZWY4MiIsImNsaWVudFNlY3JldCI6IkJiU1F1SlZOcXh0UWVEc0gifQ.rAtLgCqQErE65p5IvIU2FTENiT8XmsESuEuMRtQ8Grs"

BASE_URL = "http://4.224.186.213/evaluation-service"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}","Content-Type": "application/json"}

@app.route("/")
def home():
    return "Vehicle Scheduling Backend Running"
@app.route("/depots")
def depots():
    response = requests.get(f"{BASE_URL}/depots",headers=headers)
    return jsonify(response.json()), response.status_code


@app.route("/vehicles")
def vehicles():
    response = requests.get(f"{BASE_URL}/vehicles",headers=headers)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True)