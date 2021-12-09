from flask import Flask, request, jsonify
import re
import requests
import json

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    string = request.args.get('string')
    returnType = request.args.get('returnType')
    downloadType = request.args.get('downloadType')
    print(string, returnType, downloadType)

    
   
    link = 'http://127.0.0.1:8000/checkstring?string='+string+'&responseType='+returnType
    result = requests.post(link)
    data = result.text

    baseDict={}
    if returnType=="txt":
        d=data.replace(':', '')
        d = d.split("\n")
        print(d)
        for p in d:
            values = p.split(' ')
            baseDict[values[0]]= values[1]
    elif returnType=="json":
        d=json.loads(data)
        baseDict["Lowercase"]= d["lower_case"]
        baseDict["Numbers"]= d["numbers"]
        baseDict["Uppercase"]= d["upper_case"]
        baseDict["Special"]= d["special_characters"]
    elif returnType=="csv":
        d=data.split(';')
        baseDict["Uppercase"]= d[0]
        baseDict["Lowercase"]= d[1]
        baseDict["Numbers"]= d[2]
        baseDict["Special"]= d[3]
    elif returnType=="xml":
        d = re.findall(r'\d+', data) 
        baseDict["Uppercase"]= d[0]
        baseDict["Lowercase"]= d[1]
        baseDict["Numbers"]= d[2]
        baseDict["Special"]= d[3]
    
    returnData=""
    
    if downloadType=="txt":
         returnData="Lowercase: "+str(baseDict["Lowercase"])+"\n"+"Uppercase: "+str(baseDict["Uppercase"])+"\n"+"Numbers: "+str(baseDict["Numbers"])+"\n"+"Special: "+str(baseDict["Special"])
    elif downloadType=="json":
        returnData=json.dumps(baseDict)
    elif downloadType=="xml":
        returnData = "<string-result id=\"" + string + "\">"
        returnData += "\t<param class=\"upper_case\">" + str(baseDict["Uppercase"]) + "</param>"
        returnData += "\t<param class=\"lower_case\">" + str(baseDict["Lowercase"]) + "</param>"
        returnData += "\t<param class=\"numbers\">" + str(baseDict["Numbers"]) + "</param>"
        returnData += "\t<param class=\"special_chars\">" + str(baseDict["Special"]) + "</param>"
        returnData += "</string-result>"
    elif downloadType=="csv":
        returnData += str(baseDict["Uppercase"])
        returnData += ";"
        returnData += str(baseDict["Lowercase"])
        returnData += ";"
        returnData += str(baseDict["Numbers"])
        returnData += ";"
        returnData += str(baseDict["Special"])


    return returnData

@app.route('/convertString',  methods=['GET', 'POST'])
def convertString():
    string = request.args.get('string')
    inputType = request.args.get('inputType')
    downloadType = request.args.get('downloadType')

    data = string

    baseDict={}
    if inputType=="txt":
        d=data.replace(':', '')
        d = d.split("\n")
        print(d)
        for p in d:
            values = p.split(' ')
            baseDict[values[0]]= values[1]
    elif inputType=="json":
        d=json.loads(data)
        baseDict["Lowercase"]= d["lower_case"]
        baseDict["Numbers"]= d["numbers"]
        baseDict["Uppercase"]= d["upper_case"]
        baseDict["Special"]= d["special_characters"]
    elif inputType=="csv":
        d=data.split(';')
        baseDict["Uppercase"]= d[0]
        baseDict["Lowercase"]= d[1]
        baseDict["Numbers"]= d[2]
        baseDict["Special"]= d[3]
    elif inputType=="xml":
        d = re.findall(r'\d+', data) 
        baseDict["Uppercase"]= d[0]
        baseDict["Lowercase"]= d[1]
        baseDict["Numbers"]= d[2]
        baseDict["Special"]= d[3]
    
    returnData=""
    
    if downloadType=="txt":
         returnData="Lowercase: "+str(baseDict["Lowercase"])+"\n"+"Uppercase: "+str(baseDict["Uppercase"])+"\n"+"Numbers: "+str(baseDict["Numbers"])+"\n"+"Special: "+str(baseDict["Special"])
    elif downloadType=="json":
        returnData=json.dumps(baseDict)
    elif downloadType=="xml":
        returnData = "<string-result id=\"" + string + "\">"
        returnData += "\t<param class=\"upper_case\">" + str(baseDict["Uppercase"]) + "</param>"
        returnData += "\t<param class=\"lower_case\">" + str(baseDict["Lowercase"]) + "</param>"
        returnData += "\t<param class=\"numbers\">" + str(baseDict["Numbers"]) + "</param>"
        returnData += "\t<param class=\"special_chars\">" + str(baseDict["Special"]) + "</param>"
        returnData += "</string-result>"
    elif downloadType=="csv":
        returnData += str(baseDict["Uppercase"])
        returnData += ";"
        returnData += str(baseDict["Lowercase"])
        returnData += ";"
        returnData += str(baseDict["Numbers"])
        returnData += ";"
        returnData += str(baseDict["Special"])


    return returnData

app.run(host="localhost", port=8001, debug=False)
