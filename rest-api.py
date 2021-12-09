from flask import Flask, request, jsonify
import re
import requests
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/find_company/<string>')
def find(string):
    html = requests.get("https://panoramafirm.pl/szukaj?k={keyword}&l=".format(keyword=key_word)).text
    soup = BeautifulSoup(html, features="html.parser")

app.run(host="localhost", port=8001, debug=False)

