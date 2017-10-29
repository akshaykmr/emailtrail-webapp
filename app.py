from bottle import request, response, HTTPResponse, Bottle
from emailtrail import (
    analyse,
    analyse_hop,
    extract_protocol,
    extract_from_label,
    extract_received_by_label,
    extract_timestamp
)


app = Bottle()
version = 1.00


@app.get('/api/v1/health')
def health():
    return HTTPResponse(status=200)


@app.get('/api/v1/version')
def version():
    return HTTPResponse(version, status=200)


@app.get('/')
def index():
    response.content_type = 'text/plain; charset=utf-8'
    return 'hello'


@app.post('/api/v1/analyse')
def email_analysis():
    return {"analysis": analyse(request.body.read())}


@app.post('/api/v1/analyse_hop')
def hop_analysis():
    return {"hop_analysis": analyse_hop(request.body.read())}


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
