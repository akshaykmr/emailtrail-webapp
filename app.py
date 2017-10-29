#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import default_app, request, route, response, get

bottle.debug(True)


@get('/')
def index():
    response.content_type = 'text/plain; charset=utf-8'
    return 'hello'


bottle.run(host='0.0.0.0', port=argv[1])