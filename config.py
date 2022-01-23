import json

arroba=""

username=""

apibot=""

password=""

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

    pass
