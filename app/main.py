from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask
import rq_dashboard

rq_app = Flask(__name__)
rq_app.register_blueprint(rq_dashboard.blueprint,url_prefix="/rq")

app = FastAPI()

app.mount("/dashboard/", WSGIMiddleware(rq_app))