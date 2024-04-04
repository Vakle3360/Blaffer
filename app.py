import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory

CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, fornavn TEXT, efternavn TEXT, alder INTEGER, email TEXT, adgangskode TEXT);"
)

CREATE_BILER_TABLE = (
    "CREATE TABLE IF NOT EXISTS biler (ejer_id INTEGER, bilmærke TEXT, farve_på_bilen TEXT);"
)

INSERT_USER_RETURN_ID = "INSERT INTO users (fornavn, efternavn, alder, email, adgangskode) VALUES (%s, %s, %s, %s, %s) RETURNING id;"

INSERT_BIL = "INSERT INTO biler (ejer_id, bilmærke, farve_på_bilen) VALUES (%s, %s, %s);"

GET_USERS = (
    "SELECT * FROM users;"
)

GET_BILER = (
    "Select * FROM biler;"
)

FIND_USER = (
    "SELECT * FROM users WHERE id=%s;"
)

FIND_BILER = (
    "SELECT * FROM biler WHERE ejer_id=%s;"
)

load_dotenv()

app = Flask(__name__, static_folder="frontend/build", static_url_path='')
CORS(app)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.post("/api/user")
@cross_origin()
def create_user():
    data = request.get_json()
    fornavn = data["fornavn"]
    efternavn = data["efternavn"]
    alder = data["alder"]
    email = data["email"]
    adgangskode = data["adgangskode"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(INSERT_USER_RETURN_ID, (fornavn, efternavn, alder, email, adgangskode,))
            user_id = cursor.fetchone()[0]
    return {"id": user_id, "message": f"User ({fornavn} {efternavn}) has been created!"}, 201

@app.post("/api/bil")
@cross_origin()
def create_bil():
    data = request.get_json()
    ejer = data["ejer_id"]
    bilmærke = data["bilmærke"]
    farve = data["farve_på_bilen"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_BILER_TABLE)
            cursor.execute(INSERT_BIL, (ejer, bilmærke, farve,))
    return {"message": f"Car has been created!"}, 201

@app.get("/api/get/users")
@cross_origin()
def get_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_USERS)
            users = cursor.fetchall()
            users = list(users)
            final = []
            for i in users:
                user = i
                user_ = [
                    {
                        "id": user[0],
                        "fornavn": user[1],
                        "efternavn": user[2],
                        "alder": user[3],
                        "email": user[4],
                        "password": user[5]
                    }
                ]
                final.append(user_)
    return jsonify({"users": final})

@app.get("/api/get/biler")
@cross_origin
def get_biler():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_BILER)
            biler = cursor.fetchall()
            biler = list(biler)
    return jsonify({"biler": biler})

def find_user(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(FIND_USER, (id,))
            user = cursor.fetchone()[0]
    return {"message": f"{user}"}, 201

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')