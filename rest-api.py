from flask import Flask, Response, render_template
from bs4 import BeautifulSoup
import requests
import vobject

database = []

app = Flask(__name__)

@app.route('/find/<word>')
def checkString(word):
    html = requests.get("https://panoramafirm.pl/szukaj?k={keyword}&l=".format(keyword=word)).text
    soup = BeautifulSoup(html, features="html.parser")
    lst = soup.find('ul', {"id": "company-list"})
    return "OK"

app.run(host="localhost", port=8001, debug=False)
