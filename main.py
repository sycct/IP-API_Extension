#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/get_ip_info/<string:ip>')
def get_ip_info(ip):
    try:
        request_ip = requests.get('http://ip-api.com/json/{}?fields=16515071&lang=zh-CN'.format(ip))
        response_text = request_ip.json()
    except:
        response_text = {'status': 'error'}

    return jsonify(response_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
