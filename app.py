import os
from bottle import request, HTTPResponse, Bottle, static_file
from emailtrail import (
    analyse_headers,
    analyse_single_header,
    extract_protocol,
    extract_from_label,
    extract_received_by_label,
    extract_timestamp
)


app = Bottle()
version = 1.00

# ---------- static -----------#
local_path = os.path.abspath(os.path.dirname(__file__))
frontend_path = os.path.join(local_path, 'frontend')


@app.route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root=frontend_path)


@app.get('/')
def send_index():
    return static_file('index.html', root=frontend_path)


# ---------- API -------------- #

@app.get('/api/v1/health')
def health():
    return HTTPResponse(status=200)


@app.get('/api/v1/version')
def version():
    return HTTPResponse(version, status=200)


@app.post('/api/v1/analyse')
def email_analysis():
    return {"analysis": analyse_headers(request.body.read())}


@app.post('/api/v1/analyse_hop')
def hop_analysis():
    return {"hop_analysis": analyse_single_header(request.body.read())}


@app.post('/api/v1/extract_protocol')
def protocol():
    return {"protocol": extract_protocol(request.body.read())}


@app.post('/api/v1/extract_from_label')
def from_label():
    return {"from": extract_from_label(request.body.read())}


@app.post('/api/v1/extract_received_by_label')
def received_by_label():
    return {"by": extract_received_by_label(request.body.read())}


@app.post('/api/v1/extract_timestamp')
def timestamp():
    return {"timestamp": extract_timestamp(request.body.read())}
