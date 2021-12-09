# PPKWU zadanie 3
## API string

Api to count chars in given string using external API and get result in one of three types of files formats (json, csv, xml or simple text).

## Required packages:
1. Flask (```pip install flask```)
2. requests (``` pip install requests ```)

## Endpoints:

**1. /checkstring (POST)**
	
Endpoint accepts 2 arguments and return response in one of file formats 

## Arguments: 
1. "string" (type: string)
2. "responseType" (type: string)
## Response types:
1. "txt"
2. "json"
3. "xml"
4. "csv" (delimiter ;)

## Example of usage
**txt**

	http://127.0.0.1:5001/checkstring?string=Szymon&responseType=txt

response 
```
Upper case: 1
Lower case: 5
Numbers: 0
Special characters: 0
```

**csv**

	http://127.0.0.1:5001/checkstring?string=Szymon&responseType=csv

response 
```
1;5;0;0
```
