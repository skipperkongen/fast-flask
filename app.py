from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse
from flask import Flask, request
from markupsafe import escape

flask_app = Flask(__name__)


@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"


app = FastAPI()


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/home")


@app.get("/api")
def read_main():
    return {"message": "Hello World"}


app.mount("/home", WSGIMiddleware(flask_app))
