import json

from requests import api

global arroba
arroba=""

global username
username=""

global apibot

apibot =""

global password
password=""

global nube

nube=""

def LoadConfig():

    Loadjson()

    pass

def Loadjson():

    file  = open("/app/config.json","r")

    jsons = json.loads(file.read())

    arroba= jsons["arroba"]

    username=jsons["username"]

    password=jsons["password"]

    nube=jsons["nube"]

    apibot=jsons["API"]

    print(arroba)
    print(username)
    print(password)
    print(nube)
    print(apibot)

    pass
