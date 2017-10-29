from sys import argv
from bottle import run

from app import app

run(app=app,
    host='0.0.0.0',
    port=argv[1],
    server='paste')
