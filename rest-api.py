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

    global database
    database = []
    for item in lst.find_all('li', {"class": "company-item"}, recursive=False):
        name = item.find('a', {"class": "company-name"}).get_text().strip()
        address = item.find('div', {"class": "address"}).get_text().strip()
        number = item.find('a', {"class": "icon-telephone"})["title"].strip()
        email = item.find('a', {"class": "icon-envelope"})["data-company-email"].strip()
        card = vcard(name, address, number, email)
        dct = {
            "name": name,
            "address": address,
            "number": number,
            "email": email,
            "card": card
        }
        database.append(dct)
    return render_template('page.html', data=database)

@app.route('/download/<id>')
def download(id):
    card = database[int(id)]["card"]
    return Response(card.serialize(), mimetype="text/json+application+vcard",
                    headers={"Content-Disposition": "attachment;filename=wizytowka.vcf",
                             "Content-Transfer-Encoding": "binary"})

def vcard(name, address, number, email):
    card = vobject.vCard()

    card.add('fn')
    card.fn.value = name

    card.add('tel')
    card.tel.value = number
    card.tel.type_param = 'WORK'

    card.add('address')
    card.address.value = address
    card.address.type_param = 'WORK'

    card.add('email')
    card.email.value = email
    card.email.type_param = 'INTERNET'
    return card

app.run(host="localhost", port=8001, debug=False)
