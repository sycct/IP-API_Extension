#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/get_ip_info/<string:ip>', methods=['GET'])
def get_ip_info(ip):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    try:
        request_ip = requests.get('http://ip-api.com/json/{}?fields=16515071&lang=zh-CN'.format(ip), headers=headers)
        response_text = request_ip.json()
    except requests.exceptions.RequestException:
        response_text = {'status': 'error'}

    return jsonify(response_text)


if __name__ == '__main__':
    app.run()
