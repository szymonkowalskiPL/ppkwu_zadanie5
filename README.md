# PPKWU zadanie 5
## API panorama firm scrapper and vcards generator

Find specialist on www.panoramafirm.pl, get list of them with links to download automaticly generated vcards which you can add to contacts on your phone.

## Required packages:
1. Flask (```pip install flask```)
2. requests (``` pip install requests ```)
3. bs4 (``` pip install bs4 ```)
4. vobject (``` pip install vobject ```)

## Endpoints:
## **1. /find (GET, POST)**
	
Endpoint accepts 1 string argument which is your keyword to search in panoramafirm.pl

## Arguments: 
1. "string" (type: string)

## Response:
Generated html with list of specialist.

## Example of usage

http://127.0.0.1:8001/find/mechanik

response 

check example result on www.szymonkowalskipl.github.io




## **2. /download (POST)**
	
Endpoint accepts 1 argument - id of specialist. Returns and download vcf file.

## Arguments: 
1. id


## Example of usage

http://127.0.0.1:8001/download/0

**response**
File should be downloaded on your device.
(https://szymonkowalskipl.github.io/wizytowka.vcf)


