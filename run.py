from sys import argv
from bottle import run

from app import app

run(app=app,
    port=argv[1],
    server='paste')
