import os
from bottle import request, HTTPResponse, Bottle, static_file
from emailtrail import (
    analyse_headers,
    analyse_single_header,
    Hop,
)


app = Bottle()
version = 1.00

# ---------- static -----------#
local_path = os.path.abspath(os.path.dirname(__file__))
frontend_path = os.path.join(local_path, "frontend")


def _read_body() -> str:
    return request.body.read().decode("utf-8")


@app.route("/<filename:path>")
def send_static(filename):
    return static_file(filename, root=frontend_path)


@app.get("/")
def send_index():
    return static_file("index.html", root=frontend_path)


# ---------- API -------------- #


@app.get("/api/v1/health")
def health():
    return HTTPResponse(status=200)


@app.get("/api/v1/version")
def version():
    return HTTPResponse(version, status=200)


# Keep old contract


def _hop_resource(h: Hop) -> dict:
    return {
        "from": h.from_host,
        "protocol": h.protocol,
        "receivedBy": h.received_by_host,
        "timestamp": h.timestamp,
        "delay": h.delay,
    }


@app.post("/api/v1/analyse")
def email_analysis():
    trail = analyse_headers(_read_body())
    return {
        "analysis": {
            "To": trail.to_address,
            "From": trail.from_address,
            "Cc": trail.cc,
            "Bcc": trail.bcc,
            "total_delay": trail.total_delay,
            "trail": [_hop_resource(h) for h in trail.hops],
        }
    }


@app.post("/api/v1/analyse_hop")
def hop_analysis():
    hop = analyse_single_header(_read_body())
    return {"hop_analysis": _hop_resource(hop)}
