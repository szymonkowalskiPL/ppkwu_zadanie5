from flask import Flask, request, jsonify
import re
import requests
import json

app = Flask(__name__)

@app.route('/findCompany/<word>')
def checkString(word):
    print(word)
    return "OK"

app.run(host="localhost", port=8001, debug=False)
