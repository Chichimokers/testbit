import json
arroba=""

username=""

APIBOT=""

password=""

nube=""

def LoadConfig():

    Loadjson()

    pass

def Loadjson():

    jsons = json.loads(json)

    arroba= jsons["arroba"]

    username=jsons["username"]

    password=jsons["password"]

    nube=jsons["nube"]

    APIBOT=jsons["API"]

    pass
