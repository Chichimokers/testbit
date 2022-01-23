import json

class Config():

    def __init__(self) -> None:
        self.username=""
        self.password =""
        self.arroba=""
        self.nube=""
        self.apibot=""
        self.LoadConfig()
        pass    
    def LoadConfig(self):

      self.Loadjson()

    pass

    def Loadjson(self):

      file  = open("/app/config.json","r")

      jsons = json.loads(file.read())

      self.arroba= jsons["arroba"]

      self.username=jsons["username"]

      self.password=jsons["password"]

      self.nube=jsons["nube"]

      self.apibot=jsons["API"]

      print(self.arroba)
      print(self.username)
      print(self.password)
      print(self.nube)
      print(self.apibot)

      pass
